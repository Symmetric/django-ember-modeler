from django import template
from knockout_modeler.ko import ko, koData, koModel, koBindings, get_fields

register = template.Library()

def ember(values):
    """
    Emberify a QuerySet!
    """

    if not values:
        return ''
        
    field_names = get_fields(values[0])
    return ko(values, field_names)

def knockout_data(values, args=None):
    """

    """
    if not values:
        return ''

    name = None
    safe = False

    if args:
        arg_list = [arg.strip() for arg in args.split(',')]
        if len(arg_list) > 1:
            safe = True
        else:
            safe = False
        name = arg_list[0]

    field_names = get_fields(values[0])
    return koData(values, field_names, name, safe)

def knockout_model(values):
    """

    """
    if not values:
        return ''

    modelClass = values[0].__class__
    field_names = get_fields(values[0])
    return koModel(modelClass, field_names)

def knockout_bindings(values):
    """

    """
    if not values:
        return ''

    return koBindings(values[0])

register.filter(ember)
register.filter(knockout_data)
register.filter(knockout_model)
register.filter(knockout_bindings)