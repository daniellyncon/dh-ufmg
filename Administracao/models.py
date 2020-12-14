from datetime import date

import django
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models

from .managers import CustomUserManager


class Eixo(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Nome"))

    def __str__(self):
        return f"{self.name}"


class ObservacoesDocumento(models.Model):
    person = models.ForeignKey('Administracao.Documento', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(_("Data"))
    description = models.TextField(_("Observação"), max_length=2000, default='')

    class Meta:
        verbose_name_plural = "Observações do documento"


class Documento(models.Model):
    TYPES = (('1', 'Ofício'), ('2', 'Parecer'), ('3', 'Nota Técnica'), ('4', 'Amicus Curiae'),
             ('5', 'Documentos de Assistidos'), ('6', 'Petições'), ('7', 'Atas de Reuniões'), ('8', 'Administrativo'),
             ('9', 'Outros'))
    type = models.CharField(max_length=1, choices=TYPES, default='1', verbose_name='Tipo de Documento')
    recipients = models.CharField(_("Destinatários"), blank=True, null=True, default=None, max_length=150)
    date = models.DateField(_("Data"), default=django.utils.timezone.now, null=False, blank=False,
                            help_text="produção/recebimento/envio/protocolo")

    link = models.URLField(_("Link"), max_length=200, default=None, blank=True, null=True)
    prepared_by = models.ManyToManyField('Usuario', verbose_name=_("Elaborado por"), related_name="developer",)

    axis = models.ManyToManyField('Eixo', related_name="document_axis", blank=True,
                                  verbose_name="Eixos relacionados")

    tasks = models.ManyToManyField('Tarefa', related_name="document_task", blank=True,
                                   verbose_name="Tarefas relacionadas")

    def __str__(self):
        return f"Documento n°{self.id}"


class Tarefa(models.Model):
    title = models.CharField(_("Título"), max_length=50)
    deadline = models.DateField(_("Prazo"), default=django.utils.timezone.now)
    description = models.TextField(_("Descrição"), max_length=500, default='')
    responsible = models.ManyToManyField('Usuario', related_name="in_charge", verbose_name="Responsável")
    is_done = models.BooleanField(_("Feito"), default=False)

    @property
    def is_past(self):
        return self.deadline < date.today() if self.deadline else False

    @property
    def is_today(self):
        return self.deadline == date.today() if self.deadline else False

    def __str__(self):
        return f"{self.title}"


class Entidade(models.Model):
    name = models.CharField(verbose_name=_("Nome"), max_length=50, default=None)
    entity_liked = models.CharField(verbose_name=_("Ente administrativo a que se vincula"),
                                    max_length=200, default=None, blank=True, null=True)
    description = models.CharField(verbose_name=_("Descrição da atuação"), max_length=500, blank=True, null=True)
    contact = models.CharField(_("Telefone ou Email Institucional "), max_length=200, default=None, blank=True,
                               null=True)
    regional_administrativa = models.CharField(_("Regional administrativa"), blank=True, null=True, max_length=200)
    comments = models.TextField(_("Observação"), max_length=500, default=None, blank=True, null=True)

    reference_person = models.CharField(_("Nome"), max_length=200, default=None, blank=True,
                                        null=True)
    reference_person_contact = models.CharField(_("Contato"), max_length=200, default=None,
                                                blank=True, null=True, help_text="Telefone/Email")
    reference_function = models.CharField(max_length=200, blank=True, null=True, verbose_name="Função")
    reference_profission = models.CharField(max_length=200, blank=True, null=True, verbose_name="Profissão")
    reference_sector = models.CharField(help_text="Serviço/Setor a que se vincula", verbose_name="Serviço",
                                        blank=True, null=True, max_length=200)
    person = models.ManyToManyField('Atendimento.Pessoa', verbose_name="Pessoas assistidas",
                                    related_name="assisted_persons", blank=True)
    axis = models.ManyToManyField('Eixo', verbose_name='Eixos associados', blank=True, related_name="associated_axes")

    street = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("Rua"), default='')
    number = models.IntegerField(null=False, blank=False, verbose_name=_("Número"), default='')
    complement = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Complemento"))
    neighborhood = models.CharField(max_length=50, null=False, blank=False, verbose_name=_("Bairro"), default='')
    city = models.CharField(max_length=100, null=False, blank=False, verbose_name=_("Cidade"), default='')
    state = models.CharField(max_length=2, verbose_name=_("UF"), default='')

    def __str__(self):
        return f"{self.name}"

    def eixos(self):
        return ", ".join([str(p) for p in self.axis.all()])


class Endereco(models.Model):
    street = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("Rua"))
    number = models.IntegerField(null=False, blank=False, verbose_name=_("Número"))
    complement = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Complemento"))
    neighborhood = models.CharField(max_length=50, null=False, blank=False, verbose_name=_("Bairro"))
    city = models.CharField(max_length=100, null=False, blank=False, verbose_name=_("Cidade"))
    state = models.CharField(max_length=2, help_text="UF do estado", verbose_name=_("Estado"))
    person = models.OneToOneField('Atendimento.Pessoa', blank=True, null=True, on_delete=models.CASCADE)
    entity = models.OneToOneField('Entidade', blank=True, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField('Usuario', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rua {self.street} n°{self.number}"


class Plantao(models.Model):
    DAYS = (('1', 'Segunda-feira'), ('2', 'Terça-feira'), ('3', 'Quarta-feira'), ('4', 'Quinta-feira'),
            ('5', 'Sexta-feira'))
    day_of_the_week = models.CharField(max_length=1, choices=DAYS, verbose_name='Dia da semana')
    start_time = models.TimeField(verbose_name="Início do plantão")
    end_time = models.TimeField(verbose_name="Fim do plantão")
    user = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_day_of_the_week_display()} {self.start_time} {self.end_time}"


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Endereço de e-mail'), unique=True)
    is_staff = models.BooleanField(_("É da equipe"), default=True)
    is_active = models.BooleanField(_("Está ativo"), default=True)
    date_joined = models.DateField(_("Data de Entrada"), default=timezone.now)
    last_login = models.DateTimeField(_('Último login'), blank=True, null=True)

    SCHOLARSHIP_CHOICES = (('1', 'Bolsista'), ('2', 'Voluntário'))
    BOND_TYPE_CHOICES = (('1', 'Coordenador'), ('2', 'Orientador'), ('3', 'Estagiário'), ('4', 'Colaborador Eventual'))

    name = models.CharField(_("Nome"), max_length=100)
    rg = models.CharField(_("RG"), max_length=20, blank=True, null=True)
    cpf = models.CharField(_("CPF"), max_length=50, blank=True, null=True)
    cnh = models.CharField(_("CNH"), max_length=50, blank=True, null=True)
    axis = models.ManyToManyField(Eixo, related_name="eixo", verbose_name="Eixo")
    bond_type = models.CharField(_("Tipo de vínculo"), max_length=50, blank=True, null=True, choices=BOND_TYPE_CHOICES)
    phone = models.CharField(_("Telefone"), max_length=15, blank=True, null=True)
    registration = models.CharField(_("Nº de matrícula"), max_length=50, blank=True, null=True)

    course = models.CharField(_("Curso"), max_length=50, blank=True, null=True)
    university = models.CharField(_("Universidade"), max_length=50, blank=True, null=True)
    department = models.CharField(_("Departamento"), max_length=50, blank=True, null=True)

    date_fired = models.DateField(_("Data de desligamento"), default=None, blank=True, null=True)
    scholarship = models.CharField(_("Bolsista"), max_length=50, blank=True, null=True, choices=SCHOLARSHIP_CHOICES)
    scholarship_type = models.CharField(_("Tipo de bolsa"), max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name or '-'

    class Meta:
        verbose_name_plural = "Usuários"
        ordering = ['name']

    def get_phone(self):
        return self.phone or None

    def get_axis(self):
        return ", ".join([str(p) for p in self.axis.all()])


class Frase(models.Model):
    content = models.CharField(_("Conteúdo"), max_length=500)
    source = models.CharField(_("Fonte"), max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return f"Frase n°{self.id}"

    class Meta:
        verbose_name_plural = "Frases"
