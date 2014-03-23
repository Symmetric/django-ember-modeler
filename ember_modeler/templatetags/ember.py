from django import template
from ember_modeler.modeler import to_ember, to_ember_model

register = template.Library()


def ember(queryset, app='App'):
    """Emberify a QuerySet!"""
    if not queryset:
        return ''
        
    return to_ember(queryset, app_name=app)


def ember_model(model, app='App'):
    """Emberify a Model."""
    if not model:
        return ''

    return to_ember_model(model, app_name=app)


register.filter(ember)
register.filter(ember_model)