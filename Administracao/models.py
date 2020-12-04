from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.conf import settings
from django.urls import reverse
from .managers import CustomUserManager
from django.utils import timezone


class Eixo(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Nome"))

    def __str__(self):
        return self.name


class Documento(models.Model):
    TYPES = (('1', 'Ofício'), ('2', 'Parecer'), ('3', 'Nota Técnica'), ('4', 'Amicus Curiae'),
             ('5', 'Documentos de Assistidos'), ('6', 'Petições'), ('7', 'Atas de Reuniões'), ('8', 'Administrativo'),
             ('9', 'Outros'))
    type = models.CharField(max_length=1, choices=TYPES, default='1', verbose_name='Tipo de Documento')
    recipients = models.CharField(_("Destinatários"), blank=True, null=True, default=None, max_length=150)
    date = models.DateField(_("Data"), auto_now=False, null=True, blank=True,
                            help_text="produção/recebimento/envio/protocolo")
    link = models.URLField(_("Link"), max_length=50, default=None, blank=True, null=True)
    prepared_by = models.ManyToManyField('Usuario', verbose_name=_("Elaborado por"), blank=True,
                                         related_name="developer")
    axis = models.ManyToManyField('Eixo', related_name="document_axis", blank=True)
    tasks = models.ManyToManyField('Tarefa', related_name="document_task", blank=True)

    def __str__(self):
        return f"Documento n°{self.id}"



class Tarefa(models.Model):
    title = models.CharField(_("Título"), max_length=50)
    deadline = models.DateField(_("Prazo"), auto_now=False, auto_now_add=False, default=None, blank=True, null=True)
    description = models.TextField(_("Descrição"), max_length=500, blank=True, null=True)
    responsible = models.ManyToManyField('Usuario', related_name="in_charge", blank=True, verbose_name="Responsável")
    is_done = models.BooleanField(("Feito"), default=False)

    def __str__(self):
        return f"{self.title}"


class Entidade(models.Model):
    name = models.CharField(verbose_name=_("Nome"), max_length=50, default=None)
    entity_liked = models.CharField(verbose_name=_("Ente Administrativo a que se vincula"),
                                    max_length=200, default=None, blank=True, null=True)
    description = models.CharField(verbose_name=_("Descrição da atuação"), max_length=500, default='')
    contact = models.CharField(_("Telefone ou Email Institucional "), max_length=200, default=None, blank=True,
                               null=True)
    reference_person = models.CharField(_("Nome da pessoa de referência"), max_length=200, default=None, blank=True,
                                        null=True)
    reference_person_contact = models.CharField(_("Contato da pessoa de referência"), max_length=200, default=None,
                                                blank=True, null=True)
    comments = models.TextField(_("Observação"), max_length=500, default=None, blank=True, null=True)
    person = models.ManyToManyField('Atendimento.Pessoa', verbose_name="Pessoas assistidas",
                                    related_name="assisted_persons", blank=True)

    street = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("Rua"), default='')
    number = models.IntegerField(null=False, blank=False, verbose_name=_("Número"), default='')
    complement = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Complemento"))
    neighborhood = models.CharField(max_length=50, null=False, blank=False, verbose_name=_("Bairro"), default='')
    city = models.CharField(max_length=100, null=False, blank=False, verbose_name=_("Cidade"), default='')
    state = models.CharField(max_length=2, verbose_name=_("UF"), default='')

    axis = models.ManyToManyField('Eixo', verbose_name='Eixos associados', related_name="associated_axes")

    def __str__(self):
        return self.name

    def eixos(self):
        return ",".join([str(p) for p in self.axis.all()])


class Endereco(models.Model):
    street = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("Rua"))
    number = models.IntegerField(null=False, blank=False, verbose_name=_("Número"))
    complement = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("Complemento"))
    neighborhood = models.CharField(max_length=50, null=False, blank=False, verbose_name=_("Bairro"))
    city = models.CharField(max_length=100, null=False, blank=False, verbose_name=_("Cidade"))
    state = models.CharField(max_length=2, help_text="UF do estado", verbose_name=_("Estado"))
    person = models.ForeignKey('Atendimento.Pessoa', blank=True, null=True, on_delete=models.CASCADE)
    entity = models.OneToOneField('Entidade', blank=True, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField('Usuario', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.street


class Plantao(models.Model):
    DAYS = (('1', 'Segunda-feira'), ('2', 'Terça-feira'), ('3', 'Quarta-feira'), ('4', 'Quinta-feira'),
            ('5', 'Sexta-feira'))
    day_of_the_week = models.CharField(max_length=1, choices=DAYS, verbose_name='Dia da semana')
    start_time = models.TimeField(verbose_name="Início do plantão")
    end_time = models.TimeField(verbose_name="Fim do plantão")
    user = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.day_of_the_week} {self.start_time} {self.end_time}'


class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Usuário"))
    SCHOLARSHIP_CHOICES = (('1', 'Bolsista'), ('2', 'Voluntário'))
    BOND_TYPE_CHOICES = (('1', 'Coordenador'), ('2', 'Orientador'), ('3', 'Estagiário'), ('4', 'Colaborador Eventual'))

    name = models.CharField(_("Nome"), max_length=100, blank=True, null=True)
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
    address = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Perfis"


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    last_login = models.DateField(_('last login'), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # def __str__(self):
    #     if self.profile is not None:
    #         return self.profile.name
    #     else:
    #         return ''

    def get_name(self):
        if self.profile:
            return self.profile.name
        else:
            return ''

    class Meta:
        verbose_name_plural = "Usuários"


class Profile(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    SCHOLARSHIP_CHOICES = (('1', 'Bolsista'), ('2', 'Voluntário'))
    BOND_TYPE_CHOICES = (('1', 'Coordenador'), ('2', 'Orientador'), ('3', 'Estagiário'), ('4', 'Colaborador Eventual'))

    name = models.CharField(_("Nome"), max_length=100, blank=True, null=True)
    rg = models.CharField(_("RG"), max_length=20, blank=True, null=True)
    cpf = models.CharField(_("CPF"), max_length=50, blank=True, null=True)
    cnh = models.CharField(_("CNH"), max_length=50, blank=True, null=True)
    bond_type = models.CharField(_("Tipo de vínculo"), max_length=50, blank=True, null=True, choices=BOND_TYPE_CHOICES)
    phone = models.CharField(_("Telefone"), max_length=15, blank=True, null=True)
    registration = models.CharField(_("Nº de matrícula"), max_length=50, blank=True, null=True)

    course = models.CharField(_("Curso"), max_length=50, blank=True, null=True)
    university = models.CharField(_("Universidade"), max_length=50, blank=True, null=True)
    department = models.CharField(_("Departamento"), max_length=50, blank=True, null=True)

    date_fired = models.DateField(_("Data de desligamento"), default=None, blank=True, null=True)

    scholarship = models.CharField(_("Bolsista"), max_length=50, blank=True, null=True, choices=SCHOLARSHIP_CHOICES)
    scholarship_type = models.CharField(_("Tipo de bolsa"), max_length=50, blank=True, null=True)

    address = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Frase(models.Model):
    content = models.TextField(_("Conteúdo"), max_length=500)
    source = models.CharField(_("Fonte"), max_length=50, default=None, blank=True, null=True)

    def __str__(self):
        return f"Frase n°{self.id}"

    class Meta:
        verbose_name_plural = "Frases"
