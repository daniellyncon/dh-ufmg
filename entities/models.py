from django.db import models
from django.utils.translation import ugettext_lazy as _
from address.models import Address
from people.models import Person
from axis.models import Axis


class Entity(models.Model):
    name = models.CharField(_("Nome"), max_length=50, default=None)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    entity_liked = models.CharField(_("Ente Administrativo a que se vincula"), max_length=200, default=None, blank=True,
                                    null=True)
    description = models.CharField(_("Descrição da atuação"), max_length=500, default=None, blank=True, null=True)
    contact = models.CharField(_("Telefone ou Email Institucional "), max_length=200, default=None, blank=True,
                               null=True)
    reference_person = models.CharField(_("Pessoa de referência"), max_length=200, default=None, blank=True, null=True)
    reference_person_contact = models.CharField(_("Contato da pessoa de referência"), max_length=200, default=None,
                                                blank=True, null=True)
    comments = models.CharField(_("Observação"), max_length=500, default=None, blank=True, null=True)
    person = models.ManyToManyField(Person, related_name="assisted_persons", blank=True)
    axis = models.ManyToManyField(Axis, related_name="associated_axes", blank=True)

    def __str__(self):
        return self.name

