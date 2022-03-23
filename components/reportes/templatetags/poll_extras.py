from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def replace(value, arg):
    return mark_safe(value.replace(arg, '\n'))
