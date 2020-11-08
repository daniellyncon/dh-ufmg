from django.db import models
from django.utils.translation import ugettext_lazy as _
from axis.models import Axis
from tasks.models import Task
from users.models import User


class Document(models.Model):
    TYPES = (('1', 'Ofício'), ('2', 'Parecer'), ('3', 'Nota Técnica'), ('4', 'Amicus Curiae'),
             ('5', 'Documentos de Assistidos'), ('6', 'Petições'), ('7', 'Atas de Reuniões'), ('8', 'Administrativo'),
             ('9', 'Outros'))
    type = models.CharField(max_length=3, choices=TYPES, blank=True, null=True, verbose_name='Tipo de Documento')
    recipients = models.CharField(_("Destinatários"), blank=True, null=True, default=None, max_length=150)
    date = models.DateField(_("Data [produção/recebimento/envio/protocolo]"), auto_now=False, null=True, blank=True)
    link = models.CharField(_("Link"), max_length=50, default=None)
    prepared_by = models.ManyToManyField(User, verbose_name=_("Elaborado por"), blank=True, related_name="developer")
    axis = models.ManyToManyField(Axis, related_name="document_axis")
    tasks = models.ManyToManyField(Task, related_name="document_task")

