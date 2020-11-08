from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils.translation import ugettext_lazy as _
from users.models import User
from django.db import models
from django_fsm import FSMField, transition
from datetime import datetime


class Task(models.Model):
    title = models.CharField(_("Título"), max_length=50, default=None)
    deadline = models.DateField(_("Prazo"), auto_now=False, auto_now_add=False, default=None)
    description = models.TextField(_("Descrição"), max_length=500, blank=True, null=True)
    responsible = models.ManyToManyField(User, related_name="in_charge", blank=True)
    workflow_state = FSMField(default='draft')

    @transition(field=workflow_state, source='draft', target='published')
    def publish(self):
        print('Stage changed from draft to published')
        channel_layer = get_channel_layer()
        timestamp = str(datetime.now())
        deadline = str(self.deadline)
        responsible = []
        for q in (self.responsible.all().values('id', )):
            responsible.append(q['id'])
        async_to_sync(channel_layer.group_send)(
            'workflow', {
                'timestamp': timestamp,
                'type': 'workflow.update',
                'workflow_state': 'draft',
                'task_id': self.id,
                'task_title': self.title,
                'task_deadline': deadline,
                'task_responsible': str(responsible),
                'task_description': self.description
            }
        )

    @transition(field=workflow_state, source='published', target='draft')
    def retract(self):
        print('Stage published from draft to draft')
        channel_layer = get_channel_layer()
        timestamp = str(datetime.now())
        responsible = []
        for q in (self.responsible.all().values('id', )):
            responsible.append(q['id'])

        print(str(responsible))
        async_to_sync(channel_layer.group_send)(
            'workflow', {
                'timestamp': timestamp,
                'type': 'workflow.update',
                'workflow_state': 'draft',
                'task_id': self.id,
                'task_title': self.title,
                'task_deadline': str(self.deadline),
                'task_responsible': str(responsible),
                'task_description': self.description
            }
        )
