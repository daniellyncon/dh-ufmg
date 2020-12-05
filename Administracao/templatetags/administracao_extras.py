from django import template
from django.db.models import F  

from ..models import Frase, Tarefa
from random import choice

register = template.Library()

@register.simple_tag
def random_phrase():
    phrases = Frase.objects.all()
    return choice(phrases) if phrases else None

@register.simple_tag
def pending_tasks(user):
    return (Tarefa.objects
        .filter(responsible=user, is_done=False)
        .order_by(F('deadline').asc(nulls_last=True)))
