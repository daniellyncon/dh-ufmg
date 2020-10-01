from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Entity(models.Model):
    name = models.CharField(_("Nome"), max_length=50, default=None)