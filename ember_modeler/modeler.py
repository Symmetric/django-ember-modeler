from django.template.loader import render_to_string
import cgi
import simplejson as json
import datetime


def get_fields(model):
    try:
        if hasattr(model, "ember_fields"):
            fields = model.ember_fields()
        else:
            try:
                fields = model.to_dict().keys()
            except Exception as e:
                fields = model._meta.get_all_field_names()

        return fields

    # Crash proofing
    except Exception as e:
        return []


def to_ember_model(model, field_names=None, data=None):
    try:
        if type(model) == str:
            modelName = model
        else:
            modelName = model.__name__

        if field_names:
            fields = field_names
        else:
            fields = get_fields(model)

        if hasattr(model, "comparator"):
            comparator = str(model.comparator())
        else:
            comparator = 'id' 

        modelViewString = render_to_string("ember_modeler/model.html", {'modelName': modelName, 'fields': fields, 'data': data, 'comparator': comparator} )

        return modelViewString
    except Exception as e:
        return ''


def to_ember_bindings(model):
    try:
        if type(model) == str:
            modelName = model
        else:
            modelName = model.__class__.__name__

        modelBindingsString = "ko.applyBindings(new " + modelName + "ViewModel(), $('#" + modelName.lower() + "s')[0]);"
        return modelBindingsString

    except Exception as e:
        return ''


def to_ember_data(queryset, field_names=None, name=None, safe=False):
    try:
        modelName = queryset.model.__name__
        modelNameData = []

        if field_names:
            fields = field_names
        else:
            fields = get_fields(queryset)

        for obj in queryset:
            temp_dict = dict()
            for field in fields:
                try:
                    attribute = getattr(obj, str(field))

                    if not safe:
                        if isinstance(attribute, basestring):
                            attribute = cgi.escape(attribute)

                    temp_dict[field] = attribute
                except Exception as e:
                    continue
            modelNameData.append(temp_dict)

        if name:
            modelNameString = name
        else:
            modelNameString = modelName + "Data"

        dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime)  or isinstance(obj, datetime.date) else None
        return "var " + modelNameString + " = " + json.dumps(modelNameData, default=dthandler) + ';'
    except Exception as e:
        return ''


def to_ember(queryset, field_names=None):
    try:
        ember_data_string = to_ember_data(queryset, field_names)
        ember_model_string = to_ember_model(queryset[0].__class__.__name__, field_names, data=True)
        ember_bindings_string = to_ember_bindings(queryset[0])

        ember_string = ember_data_string + '\n' + ember_model_string + '\n' + ember_bindings_string

        return ember_string
    except Exception as e:
        return ''
