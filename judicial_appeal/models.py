from django.db import models
from django.utils.translation import ugettext_lazy as _
from law_suits.models import LawSuit


class JudicialAppeal(models.Model):
    TYPES = (('1', 'Apelação'), ('2', 'Agravo de instrumento'), ('3', 'Embargos de declaraçã'), ('4', 'Agravo interno'),
             ('5', 'Recurso ordinário'), ('6', 'Recurso extraordinário'), ('7', 'Recurso especial'),
             ('8', 'Habeas corpus'),
             ('9', 'Recurso em sentido estrito'), ('10', 'Agravo em execução'), ('11', 'Outro'))
    type = models.CharField(max_length=3, choices=TYPES, blank=True, null=True, verbose_name='Categoria')
    judicial_appeal_number = models.CharField(_("Número do Recurso"), max_length=50,
                                              default=None, blank=True, null=True)
    plenary = models.CharField(_("Câmara/Turma/Plenário"), max_length=200, default=None, blank=True, null=True)
    report = models.CharField(_("Relatoria"), max_length=200, default=None, blank=True, null=True)
    resume = models.TextField(_("Resumo"), max_length=5000, default=None, blank=True, null=True)
    law_suit = models.ForeignKey(LawSuit, on_delete=models.CASCADE)

    def __str__(self):
        return self.judicial_appeal_number


class JudicialAppealMove(models.Model):
    judicial_appeal = models.ForeignKey(JudicialAppeal, on_delete=models.CASCADE)
    date = models.DateField(_("Data"), auto_now=True)
    description = models.CharField(_("Descrição"), max_length=1000, default=None, blank=True, null=True)
