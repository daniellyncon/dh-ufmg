from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Document(models.Model):
    type = models.CharField(_("Link"), max_length=50)