from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class LawSuit(models.Model):
    law_suit_number = models.CharField(_("Número do processo"), max_length=50, default=None)