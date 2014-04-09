from django.db.models.fields import AutoField, IntegerField, FloatField, DateField, BooleanField
from django.template.loader import render_to_string


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


def get_field_type(model, field_name):
    field = model._meta.get_field_by_name(field_name)[0]

    if (isinstance(field, AutoField) or
            isinstance(field, IntegerField) or
            isinstance(field, FloatField)):
        return 'number'
    elif isinstance(field, DateField):
        return 'date'
    elif isinstance(field, BooleanField):
        return 'bool'
    else:
        return 'string'


def to_ember_model(model, field_names=None, app_name='App', id_='id'):
    try:
        model_name = model.__class__.__name__

        if field_names:
            fields = field_names
        else:
            fields = get_fields(model)

        fields = {field: get_field_type(model, field) for field in fields}
        # Don't include the PK.
        del(fields[id_])

        modelViewString = render_to_string(
            "ember_modeler/model.html",
            {
                'model_name': model_name,
                'fields': fields,
                'app': app_name,
            })

        return modelViewString
    except Exception as e:
        return ''


def to_ember(queryset, field_names=None, app_name='App'):
    try:
        ember_string = to_ember_model(queryset.model, field_names, app_name=app_name)
        return ember_string
    except Exception as e:
        return ''
