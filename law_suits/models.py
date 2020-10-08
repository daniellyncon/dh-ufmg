from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class LawSuit(models.Model):
    AREAS_CHOICES = (('1', 'Administrativo'), ('2', 'Ambiental'), ('3', 'Cível'), ('4', 'Consumidor'),
                    ('5', 'Criminal'), ('6', 'Família'), ('7', 'Previdenciário'), 
                    ('8', 'Sucessões'), ('9', 'Societário'), ('10', 'Trabalhista'), 
                    ('11', 'Tributário'), ('12', 'Contratos'), ('13', 'Internacional'),
                    ('14', 'Retificação') )
    law_suit_number = models.CharField(_("Número do processo"), max_length=50, default=None)
    action_type = models.CharField( ("Tipo de ação"), max_length=200, default=None)
    open_mandate = models.BooleanField(_("Mandado de prisão em aberto"), default=None)
    district = models.CharField( ("Comarca"), max_length=200, default=None)
    law_area = models.CharField(verbose_name="Área do direito", choices=AREAS_CHOICES, max_length=50, blank=True, null=True)
    latest_moves = models.CharField(_("Últimas movimentações"), max_length=500, default=None)
    has_lawyer = models.BooleanField(_("Possui advogado/defensor constituído nos autos"), default=None)
    lawyer_name = models.CharField( ("Nome advogado/defensor"), max_length=200, default=None, null=True, blank=True)
    lawyer_contact = models.CharField( ("Contato advogado/defenso"), max_length=200, default=None, null=True, blank=True)
    followed_by_daj = models.BooleanField(_("Acompanhado pela DAJ"), default=None)
    minhadaj_number = models.CharField(_("Número MinhaDAJ"), max_length=50, default=None, null=True, blank=True)
    start_date = models.DateField(_("Data início [PI/recebimento da denúncia]"), auto_now=False, default=None)
    transit_date = models.DateField(_("Data trânsito em julgado"), auto_now=False, default=None)







    

