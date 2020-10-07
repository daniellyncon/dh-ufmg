from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Task(models.Model):
    title = models.CharField(_("Título"), max_length=50, default=None)
    deadline = models.DateField(_("Prazo"), auto_now=False, auto_now_add=False, default=None)