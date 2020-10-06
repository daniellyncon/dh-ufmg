from django.db import models
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    street = models.CharField(_("Rua"), max_length=100, blank=True, null=True)
    number = models.IntegerField(_("Número"), blank=True, null=True)
    complement = models.CharField(_("Complemento"), max_length=100, blank=True, null=True)
    neighborhood = models.CharField(_("Bairro"), max_length=100, blank=True, null=True)
    city = models.CharField(_("Cidade"), max_length=50, blank=True, null=True)
    state = models.CharField(_("Estado"), max_length=50, blank=True, null=True)
