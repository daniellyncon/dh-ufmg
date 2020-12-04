from django import template

from ..models import Frase

register = template.Library()

@register.simple_tag
def random_phrase():
    return Frase.objects.order_by('?').first()
