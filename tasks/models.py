from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import User


class Task(models.Model):
    title = models.CharField(_("Título"), max_length=50, default=None)
    deadline = models.DateField(_("Prazo"), auto_now=False, auto_now_add=False, default=None)
    description = models.TextField(_("Descrição"), max_length=500, blank=True, null=True)
    responsible = models.ManyToManyField(User, related_name="in_charge", blank=True)
