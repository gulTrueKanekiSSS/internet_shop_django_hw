from django import template

register = template.Library()


@register.filter
def truncate_after_100(text):
    if len(text) > 100:
        return text[:100] + '...'
    else:
        return text