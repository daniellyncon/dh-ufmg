from django import template
from ..models import Frase
from random import choice

register = template.Library()

@register.simple_tag
def random_phrase():
    phrases = Frase.objects.all()
    return choice(phrases) if phrases else None
