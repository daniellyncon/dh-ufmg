from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from axis.models import Axis


class OnDuty(models.Model):
    day_of_the_week = models.IntegerField(verbose_name="Dia da semana")
    start_time = models.TimeField()
    end_time = models.TimeField()


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, default=None, max_length=50)
    first_name = models.CharField(blank=True, null=True, default=None, max_length=50)
    last_name = models.CharField(blank=True, null=True, default=None, max_length=50)
    name = models.CharField(_("Nome"), max_length=100)
    email = models.EmailField(_('Email'), unique=True)
    axis = models.ForeignKey(Axis, verbose_name=_("Eixo"), on_delete=models.SET_NULL, blank=True, null=True)
    bond_type = models.CharField(_("Tipo de vínculo"), max_length=50, blank=True, null=True)
    phone = models.CharField(_("Telefone"), max_length=15, blank=True, null=True)
    registration = models.CharField(_("Nº de matrícula"), max_length=50, blank=True, null=True)
    street_address = models.CharField(_("Rua"), max_length=100, blank=True, null=True)
    number_address = models.IntegerField(_("Número"), blank=True, null=True)
    complement_address = models.CharField(_("Complemento"), max_length=100, blank=True, null=True)
    neighborhood_address = models.CharField(_("Bairro"), max_length=100, blank=True, null=True)
    city_address = models.CharField(_("Cidade"), max_length=50, blank=True, null=True)
    state_address = models.CharField(_("Estado"), max_length=50, blank=True, null=True)
    course = models.CharField(_("Curso"), max_length=50, blank=True, null=True)
    university = models.CharField(_("Universidade"), max_length=50, blank=True, null=True)
    department = models.CharField(_("Departamento"), max_length=50, blank=True, null=True)
    rg = models.CharField(_("RG"), max_length=20)
    cpf = models.CharField(_("CPF"), max_length=50)
    cnh = models.CharField(_("CNH"), max_length=50, blank=True, null=True)
    date_joined = models.DateField(_("Data de entrada na CDH"), auto_now=False)
    date_fired = models.DateField(_("Data de desligamento"), auto_now=False)
    is_active = models.BooleanField(_("Ativo"), default=True)

    scholarship = models.CharField(_("Bolsista"), max_length=50, blank=True, null=True)
    scholarship_type = models.CharField(_("Tipo de bolsa"), max_length=50, blank=True, null=True)
    on_duty = models.ForeignKey(OnDuty, verbose_name="Plantão", on_delete=models.SET_NULL, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'date_joined', 'rg', 'cpf',
                       'axis', 'bond_type', 'university']

    def __str__(self):
        return self.name
