from django.db import models
from law_suits.models import LawSuit

# Create your models here.

class JudicialAppeal(models.Model):

    TYPES = (('1', 'apelação'), ('2', 'agravo de instrumento'), ('3', 'embargos de declaraçã'), ('4', 'agravo interno'),
            ('5', 'recurso ordinário'), ('6', 'recurso extraordinário'), ('7', 'recurso especial'), ('8', 'habeas corpus'),
            ('9', 'recurso em sentido estrito'), ('10', 'agravo em execução'), ('11', 'Outro'))
    type = models.CharField(max_length=3, choices=TYPES, blank=True, null=True, verbose_name='Categoria')
    judicial_appeal_number = models.CharField(("Número do Recurso"), max_length=50, default=None, blank=True, null=True)
    plenary = models.CharField( ("Câmara/Turma/Plenário"), max_length=200, default=None, blank=True, null=True)
    report = models.CharField( ("Relatoria"), max_length=200, default=None, blank=True, null=True)
    resume = models.CharField( ("Resumo"), max_length=5000, default=None, blank=True, null=True)
    law_suit = models.ForeignKey(LawSuit, on_delete=models.CASCADE)

    
