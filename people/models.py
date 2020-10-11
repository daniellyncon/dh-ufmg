from django.db import models
from users.models import User
# from cases.models import Case
from documents.models import Document
from datetime import date
from address.models import Address


class Person(models.Model):
    CIVIL_STATUS_CHOICES = (('1', 'Solteira'), ('2', 'Casada'), ('3', 'Separada'), ('4', 'Divorciada'),
                            ('5', 'Viúva'))

    GENDER_CHOICES = (('1', 'Agênero'), ('2', 'Cisgênero'), ('3', 'Gênero fluido'), ('4', 'Transgênero'),
                      ('5', 'Crossdresser'), ('6', 'Drag Queen'), ('7', 'Não-binário'))

    SCHOOLING_CHOICES = (('1', 'Ensino fundamental incompleto'), ('2', 'Ensino fundamental completo'),
                         ('3', 'Ensino médio incompleto'), ('4', 'Ensino médio completo'),
                         ('5', 'Ensino superior incompleto'), ('6', 'Ensino superior completo'))

    CASE_BOND_CHOICES = (('1', 'assistido'), ('2', 'jurisdicionado'), ('3', 'atingido'), ('4', 'terceiro'),
                         ('5', 'interessado'), ('6', 'outro'))

    LAW_SUIT_CHOICES = (('1', 'parte autora'), ('2', 'parte ré'), ('3', 'terceiro'), ('4', 'interessado'))

    assisted = models.BooleanField(verbose_name="Pessoa assistida?", blank=True, null=True)
    responsible_advisor = models.ManyToManyField(User, verbose_name="Orientadora responsável", related_name="p_advisor")
    responsible_intern = models.ManyToManyField(User, verbose_name="Estagiária responsável", related_name="p_intern")
    first_appointment_date = models.DateField(blank=True, null=True)
    full_name = models.CharField(verbose_name="Nome completo", max_length=100, default="")
    mother_name = models.CharField(verbose_name="Nome da mãe", max_length=100, default="")

    civil_registry = models.CharField(verbose_name="Registro civil", max_length=100, blank=True, null=True)
    civil_status = models.CharField(verbose_name="Estado civíl", choices=CIVIL_STATUS_CHOICES, max_length=50, blank=True, null=True)
    schooling = models.CharField(verbose_name="Escolaridade", choices=SCHOOLING_CHOICES, max_length=50, blank=True, null=True)

    # Identificação
    rg = models.CharField(verbose_name="RG", max_length=20, blank=True, null=True)
    cpf = models.CharField(verbose_name="CPF", max_length=50, blank=True, null=True)
    cnh = models.CharField(verbose_name="CNH", max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)

    # Contato
    email = models.EmailField(verbose_name="E-mail", blank=True, null=True)
    phone = models.CharField(verbose_name="Telefone", max_length=20, blank=True, null=True)
    reference_regional_administration = models.CharField(verbose_name="Regional Administrativa de Referência",
                                                         max_length=100, blank=True, null=True)
    # Como se identifica
    gender_identity = models.CharField(verbose_name="Identidade de gênero", max_length=50,
                                       choices=GENDER_CHOICES, blank=True, null=True)
    preferred_pronouns = models.CharField(verbose_name="Pronomes que prefere usar", max_length=100,
                                          blank=True, null=True)
    self_identification = models.CharField(verbose_name="Auto-identificação raça/cor", max_length=50,
                                           blank=True, null=True)

    # nascimento
    birthday = models.DateField(verbose_name="Data de nascimento", blank=True, null=True)
    birth_city = models.CharField(verbose_name="Cidade de nascimento", max_length=50, blank=True, null=True)
    birth_state = models.CharField(verbose_name="Cidade de nascimento", max_length=50, blank=True, null=True)

    # saúde
    has_health_problem = models.BooleanField(verbose_name="Tem algum problema de saúde?", default=None, blank=True,
                                             null=True)
    which_health_problem = models.CharField(verbose_name="Qual", default=None, blank=True, null=True, max_length=50)
    receives_assistance = models.BooleanField(verbose_name="Recebe algum auxílio?", default=None, blank=True, null=True)
    which_assistance = models.CharField(verbose_name="Qual auxílio", default=None, blank=True, null=True, max_length=50)
    related_person = models.ForeignKey('self', blank=True, null=True, related_name='p_person',
                                       verbose_name="Pessoa relacionada", on_delete=models.SET_NULL)
    related_person_bond = models.CharField(verbose_name="Vínculo", max_length=30, blank=True, null=True)

    # contato
    contact_email = models.EmailField(verbose_name="E-mail contato", blank=True, null=True)
    contact_phone = models.CharField(verbose_name="Telefone contato", max_length=20, blank=True, null=True)
    contact_address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL,
                                        related_name='contact')
    # caso
    # related_case = models.ForeignKey(Case, verbose_name="Caso relacionado", related_name="case",
    #                                 blank=True, null=True)
    related_case_bond = models.CharField("Vínculo caso", max_length=30, blank=True, null=True,
                                         choices=CASE_BOND_CHOICES)

    # processo

    related_law_suit_bond = models.CharField(verbose_name="Vínculo processo", choices=LAW_SUIT_CHOICES,
                                             max_length=50, blank=True, null=True)

    document = models.ManyToManyField(Document, verbose_name="Documentos", blank=True)

    def __str__(self):
        return self.full_name