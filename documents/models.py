from django.db import models
from django.utils.translation import ugettext_lazy as _
from axis.models import Axis
from tasks.models import Task
from users.models import User


class Document(models.Model):
    TYPES = (('1', 'Ofício'), ('2', 'Parecer'), ('3', 'Nota Técnica'), ('4', 'Amicus Curiae'),
             ('5', 'Documentos de Assistidos'), ('6', 'Petições'), ('7', 'Atas de Reuniões'), ('8', 'Administrativo'),
             ('9', 'Outros'))
    type = models.CharField(max_length=3, choices=TYPES, blank=True, null=True, verbose_name='TIpo de Documento')
    date = models.DateField(_("Data [produção/recebimento/envio/protocolo]"), auto_now=False, null=True, blank=True)
    prepared_by = models.ManyToManyField(User, verbose_name=_("Elaborado por"), blank=True, related_name="prepared_by")
    recipients = models.CharField(_("Destinatários"), blank=True, null=True, default=None, max_length=150)
    axis = models.ManyToManyField(Axis, related_name="document_axis")
    link = models.CharField(_("Link"), max_length=50, default=None)
    tasks = models.ManyToManyField(Task, _("Tarefas"))
