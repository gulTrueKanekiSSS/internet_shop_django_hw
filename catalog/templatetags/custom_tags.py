from django import template

register = template.Library()


@register.simple_tag
def image_tag(image_url, alt_text=''):
    return f'<img src="/media/{image_url}" class="img-fluid rounded" alt="{alt_text}">'

