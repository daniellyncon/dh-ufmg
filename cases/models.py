from django.db import models
from django.utils.translation import ugettext_lazy as _
from axis.models import Axis
from users.models import User
from people.models import Person
from entities.models import Entity
from lawSuits.models import LawSuit
from tasks.models import Task
from documents.models import Document


class Case(models.Model):
    AREAS = (('1', 'Administrativo'), ('2', 'Ambiental'), ('3', 'Cível'), ('4', 'Consumidor'),
                ('5', 'Criminal'))
    case_number = models.IntegerField(("Número do Caso"), blank=False, null=False)
    releted_areas = models.CharField(max_length=3, choices=AREAS, blank=True, null=True, verbose_name='Áreas Relacionadas')
    assisted_person = models.ManyToManyField(Person, verbose_name=_("Pessoa Assistida"), blank=True)
    advisor = models.ManyToManyField(User, verbose_name=_("Oritentador Responsável"),blank=True, related_name="advisor")
    intern = models.ManyToManyField(User, verbose_name=_("Estagiário Responsável"), blank=True, related_name="intern")
    axis = models.ForeignKey(Axis, verbose_name=_("Eixo"), on_delete=models.SET_NULL, blank=True, null=True)
    entities = models.ManyToManyField(Entity, verbose_name=_("Entidades relacionadas"), blank=True)
    reference_contacts = models.CharField( ("Contatos de referência"), blank=True, null=True, default=None, max_length=200)
    daj_number = models.CharField(("Número do caso no MinhaDAJ"), blank=True, null=True, default=None, max_length=50)
    daj_advisor = models.CharField(("Orientador no DAJ"), blank=True, null=True, default=None, max_length=50)
    daj_intern = models.CharField(("Estagiário no DAJ"), blank=True, null=True, default=None, max_length=50)    
    law_suits = models.ManyToManyField(LawSuit, verbose_name=("Processos"), blank=True)
    report = models.CharField( ("Relatório"), blank=True, null=True, default=None, max_length=15000)
    tasks = models.ManyToManyField(Task, verbose_name=("Processos"),blank=True)
    documents = models.ManyToManyField(Document, verbose_name=("Processos"), blank=True)
    registration_date = models.DateField(_("Data de cadastro"), auto_now=False)
    solution_date = models.DateField(_("Data de cadastro"), auto_now=False)

    def __str__(self):
        return self.case_number
