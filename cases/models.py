from django.db import models
from django.utils.translation import ugettext_lazy as _
from axis.models import Axis
from users.models import User
from people.models import Person
from entities.models import Entity
from law_suits.models import LawSuit
from tasks.models import Task
from documents.models import Document


class Case(models.Model):
    AREAS = (('1', 'Administrativo'), ('2', 'Ambiental'), ('3', 'Cível'), ('4', 'Consumidor'),
             ('5', 'Criminal'), ('6', 'Família'), ('7', 'Ambiental'), ('8', 'Previdenciário'),
             ('9', 'Sucessões'), ('10', 'Societário'), ('11', 'Trabalhista'), ('12', 'Tributário'),
             ('13', 'Contratos'), ('14', 'Internacional'))
    # case_number = models.IntegerField(("Número do Caso"), blank=False, null=False)
    related_areas = models.CharField(max_length=3, choices=AREAS, blank=True, null=True,
                                     verbose_name='Áreas Relacionadas')
    reference_contacts = models.CharField(("Contatos de referência"), blank=True, null=True, default=None,
                                          max_length=200)
    daj_number = models.CharField(("Número do caso no MinhaDAJ"), blank=True, null=True, default=None, max_length=50)
    daj_advisor = models.CharField(("Orientador no DAJ"), blank=True, null=True, default=None, max_length=50)
    daj_intern = models.CharField(("Estagiário no DAJ"), blank=True, null=True, default=None, max_length=50)
    report = models.CharField(("Relatório"), blank=True, null=True, default=None, max_length=15000)
    registration_date = models.DateField(_("Data de cadastro"), auto_now=True)
    solution_date = models.DateField(_("Data de solução"), auto_now=False, blank=True, null=True)

    advisor = models.ManyToManyField(User, verbose_name=_("Oritentador Responsável"), blank=True,
                                     related_name="advisor")
    intern = models.ManyToManyField(User, verbose_name=_("Estagiário Responsável"), blank=True, related_name="intern")
    assisted_person = models.ManyToManyField(Person, blank=True, related_name="case_people")
    law_suits = models.ManyToManyField(LawSuit, blank=True, related_name="case_law_suits")
    entities = models.ManyToManyField(Entity, blank=True, related_name="case_entities")
    axis = models.ForeignKey(Axis, verbose_name=_("Eixo"), on_delete=models.SET_NULL, blank=True, null=True)
    tasks = models.ManyToManyField(Task, blank=True, related_name="case_tasks")
    documents = models.ManyToManyField(Document, blank=True, related_name="case_documents")

    def __str__(self):
        return self.id
