from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from Administracao.models import Eixo, Tarefa, Documento, Endereco, Entidade
from datetime import date


class Caso(models.Model):
    AREAS = (('1', 'Administrativo'), ('2', 'Ambiental'), ('3', 'Cível'), ('4', 'Consumidor'),
             ('5', 'Criminal'), ('6', 'Família'), ('7', 'Ambiental'), ('8', 'Previdenciário'),
             ('9', 'Sucessões'), ('10', 'Societário'), ('11', 'Trabalhista'), ('12', 'Tributário'),
             ('13', 'Contratos'), ('14', 'Internacional'))

    related_areas = models.CharField(_('Áreas relacionadas'), max_length=3, choices=AREAS, blank=True, null=True,)
    reference_contacts = models.CharField(_("Contatos de referência"), blank=True, null=True, default=None,
                                          max_length=200)
    daj_number = models.CharField(_("Número do caso no MinhaDAJ"), blank=True, null=True, default=None, max_length=50)
    daj_advisor = models.CharField(_("Orientador no DAJ"), blank=True, null=True, default=None, max_length=50)
    daj_intern = models.CharField(_("Estagiário no DAJ"), blank=True, null=True, default=None, max_length=50)
    report = models.TextField(_("Relatório"), blank=True, null=True, default=None, max_length=15000)
    registration_date = models.DateField(_("Data de cadastro"), auto_now=False)
    solution_date = models.DateField(_("Data de solução"), auto_now=False, blank=True, null=True)

    advisor = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("Oritentador Responsável"),
                                     related_name="Orientador")
    intern = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("Estagiário Responsável"),
                                    related_name="Estagiario")
    assisted_person = models.ManyToManyField('Pessoa', verbose_name=_("Pessoa assistidas"), blank=True)
    law_suits = models.ManyToManyField('Processo', blank=True, verbose_name=_("Processos relacionados"))
    entities = models.ManyToManyField(Entidade, blank=True, verbose_name=_("Entidades relacionadas"))
    axis = models.ManyToManyField(Eixo, blank=True, verbose_name=_("Eixos relacionados"))
    tasks = models.ManyToManyField(Tarefa, blank=True, verbose_name=_("Tarefas relacionadas"))
    documents = models.ManyToManyField(Documento, blank=True, verbose_name=_("Documentos relacionados"))

    def __str__(self):
        return f"Caso n°{self.id}"

    class Meta:
        verbose_name_plural = "Casos"


class Processo(models.Model):
    AREAS_CHOICES = (('1', 'Administrativo'), ('2', 'Ambiental'), ('3', 'Cível'), ('4', 'Consumidor'),
                     ('5', 'Criminal'), ('6', 'Família'), ('7', 'Previdenciário'),
                     ('8', 'Sucessões'), ('9', 'Societário'), ('10', 'Trabalhista'),
                     ('11', 'Tributário'), ('12', 'Contratos'), ('13', 'Internacional'),
                     ('14', 'Retificação'))
    law_suit_number = models.CharField(verbose_name=_("Número do processo"), max_length=50, default=None)
    action_type = models.CharField(verbose_name=_("Tipo de ação"), max_length=200, default=None, blank=True, null=True)
    open_mandate = models.BooleanField(verbose_name=_("Mandado de prisão em aberto?"), default=None)
    district = models.CharField(verbose_name=_("Comarca"), max_length=200, default=None, blank=True, null=True)
    law_area = models.CharField(verbose_name="Área do direito", choices=AREAS_CHOICES, max_length=50, blank=True,
                                null=True)
    latest_moves = models.CharField(verbose_name=_("Últimas movimentações"), max_length=500, default=None, blank=True,
                                    null=True)
    has_lawyer = models.BooleanField(verbose_name=_("Possui advogado/defensor constituído nos autos?"), default=None)
    lawyer_name = models.CharField(verbose_name=_("Nome advogado/defensor"), max_length=200, default=None, null=True,
                                   blank=True)
    lawyer_contact = models.CharField(verbose_name=_("Contato advogado/defenso"), max_length=200, default=None,
                                      null=True, blank=True)
    followed_by_daj = models.BooleanField(verbose_name=_("Acompanhado pela DAJ"), default=None)
    minhadaj_number = models.CharField(verbose_name=_("Número MinhaDAJ"), max_length=50, default=None, null=True,
                                       blank=True)
    start_date = models.DateField(verbose_name=_("Data início [PI/recebimento da denúncia]"), auto_now=False,
                                  default=None, blank=True, null=True)
    transit_date = models.DateField(verbose_name=_("Data trânsito em julgado"), auto_now=False, default=None)
    related_people = models.ManyToManyField('Pessoa', verbose_name='Pessoas envolvidas',
                                            related_name="related_law_suit")

    def __str__(self):
        return f'Número do processo {self.law_suit_number}'

    class Meta:
        verbose_name_plural = "Processos"

    def get_pessoas(self):
        return ",".join([str(p) for p in self.related_people.all()])

    def get_law_area(self):
        return self.get_law_area_display()

    def get_recursos(self):
        return ",".join([str(p) for p in self.judicial_appeals.all()])


class Recurso(models.Model):
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
    law_suit = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name='judicial_appeals', blank=True,
                                 null=True)

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

    def __str__(self):
        return f'{self.get_type_display()} n° {self.judicial_appeal_number}'


class HistoricoRecurso(models.Model):
    judicial_appeal = models.ForeignKey(Recurso, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(_("Data"))
    description = models.TextField(_("Descrição"), max_length=1000, default='')

    class Meta:
        verbose_name_plural = "Movimentações no recurso"


class Pessoa(models.Model):
    CIVIL_STATUS_CHOICES = (('1', 'Solteira'), ('2', 'Casada'), ('3', 'Separada'), ('4', 'Divorciada'),
                            ('5', 'Viúva'))

    GENDER_CHOICES = (('1', 'Agênero'), ('2', 'Cisgênero'), ('3', 'Gênero flúido'), ('4', 'Transgênero'),
                      ('5', 'Crossdresser'), ('6', 'Drag Queen'), ('7', 'Não-binário'))

    SCHOOLING_CHOICES = (('1', 'Ensino fundamental incompleto'), ('2', 'Ensino fundamental completo'),
                         ('3', 'Ensino médio incompleto'), ('4', 'Ensino médio completo'),
                         ('5', 'Ensino superior incompleto'), ('6', 'Ensino superior completo'))

    CASE_BOND_CHOICES = (('1', 'Assistido'), ('2', 'Jurisdicionado'), ('3', 'Atingido'), ('4', 'Terceiro'),
                         ('5', 'Interessado'), ('6', 'Outro'))

    LAW_SUIT_CHOICES = (('1', 'Parte autora'), ('2', 'Parte ré'), ('3', 'Terceiro'), ('4', 'interessado'))

    assisted = models.BooleanField(verbose_name="Pessoa assistida?", blank=True, null=True)
    responsible_advisor = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="p_advisor",
                                                 verbose_name="Orientadora responsável")
    responsible_intern = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="p_intern",
                                                verbose_name="Estagiária responsável")
    first_appointment_date = models.DateField(blank=True, null=True, verbose_name="Data do primeiro atendimento")
    full_name = models.CharField(verbose_name="Nome completo", max_length=100, default="")
    mother_name = models.CharField(verbose_name="Nome da mãe", max_length=100, default="")

    civil_registry = models.CharField(verbose_name="Registro civil", max_length=100, blank=True, null=True)
    civil_status = models.CharField(verbose_name="Estado civíl", choices=CIVIL_STATUS_CHOICES, max_length=50,
                                    blank=True, null=True)
    schooling = models.CharField(verbose_name="Escolaridade", choices=SCHOOLING_CHOICES, max_length=50, blank=True,
                                 null=True)

    # Identificação
    rg = models.CharField(verbose_name="RG", max_length=20, blank=True, null=True)
    cpf = models.CharField(verbose_name="CPF", max_length=50, blank=True, null=True)
    cnh = models.CharField(verbose_name="CNH", max_length=50, blank=True, null=True)
    address = models.ForeignKey('Administracao.Endereco', on_delete=models.SET_NULL, blank=True, null=True)

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
    birthday = models.DateField(verbose_name="Data de nascimento")
    birth_city = models.CharField(verbose_name="Cidade de nascimento", max_length=50, blank=True, null=True)
    birth_state = models.CharField(verbose_name="Estado de nascimento", max_length=50, blank=True, null=True)

    # saúde
    has_health_problem = models.BooleanField(verbose_name="Tem algum problema de saúde?", default=None, blank=True,
                                             null=True)
    which_health_problem = models.CharField(verbose_name="Qual", default=None, blank=True, null=True, max_length=50)
    receives_assistance = models.BooleanField(verbose_name="Recebe algum auxílio?", default=None, blank=True, null=True)
    which_assistance = models.CharField(verbose_name="Qual auxílio", default=None, blank=True, null=True, max_length=50)

    related_person = models.CharField(max_length=50, blank=True, null=True, verbose_name="Pessoa relacionada")
    related_person_bond = models.CharField(verbose_name="Vínculo pessoa relacionada",
                                           max_length=30, blank=True, null=True)

    # ('has_health_problem', '', '', '', '', '', '', '',)
    # contato
    contact_email = models.EmailField(verbose_name=_("E-mail contato"), blank=True, null=True)
    contact_phone = models.CharField(verbose_name=_("Telefone contato"), max_length=20, blank=True, null=True)
    contact_address = models.ForeignKey('Administracao.Endereco', blank=True, null=True, on_delete=models.SET_NULL,
                                        related_name='contact')
    # caso
    related_case_bond = models.CharField(verbose_name=_("Vínculo caso"), max_length=30, blank=True, null=True,
                                         choices=CASE_BOND_CHOICES)

    # processo

    related_law_suit_bond = models.CharField(verbose_name=_("Vínculo processo"), choices=LAW_SUIT_CHOICES,
                                             max_length=50, blank=True, null=True)

    document = models.ManyToManyField('Administracao.Documento', verbose_name=_("Documentos"), blank=True)

    axis = models.ManyToManyField('Administracao.Eixo', verbose_name=_("Eixos relacionados"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Pessoas"

    def get_related_cases(self):
        return ",".join([str(c) for c in self.caso_set.all()])


class AtendimentoTranspasse(models.Model):
    FREQUENCY_HEALTH_CENTER_CHOICES = (('1', "Vou com frequência"), ('2', '1 a 3 meses atrás'),
                                       ('3', '3 a 6 meses atrás'), ('4', 'Mais de 6 meses'), ('5', 'Mais de um ano'))

    assisted_person = models.ForeignKey('Pessoa', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name="atendimento_transpasse")

    how_knew_about_transpasse = models.CharField(max_length=100, blank=True, null=True,
                                                 verbose_name="Como soube do Transpasse")
    psychology_intern = models.ForeignKey('Administracao.Usuario', verbose_name="Estagiária de psicologia responsável",
                                          blank=True, null=True, on_delete=models.SET_NULL, limit_choices_to={
            'Estagiario': True
        })
    lives_with = models.CharField(max_length=100, blank=True, null=True, verbose_name="Com quem mora")
    cities_lived = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidades por onde passou")
    ist_exams_up_to_date = models.BooleanField(default=False, blank=True, null=True, verbose_name="Exames IST em dia")
    last_time_been_health_center = models.CharField(max_length=100, blank=True, null=True,
                                                    choices=FREQUENCY_HEALTH_CENTER_CHOICES,
                                                    verbose_name="Última vez que foi ao posto de saúde")
    is_drug_user = models.BooleanField(default=False, blank=True, null=True, verbose_name="Faz uso de álcool e drogas")
    which_drugs = models.CharField(max_length=100, blank=True, null=True, verbose_name="Quais drogas usa")
    consider_drugs_bad = models.BooleanField(default=False, verbose_name="Considera o uso prejudicial")
    uses_hormones = models.BooleanField(default=False, blank=True, null=True, verbose_name="Faz uso de hormônios")
    use_accompanied_by_doctor = models.BooleanField(default=False, blank=True, null=True,
                                                    verbose_name="Uso acompanhado por médico")
    which_hormones = models.CharField(max_length=100, blank=True, null=True, verbose_name="Qual(is) hormônios")
    works = models.BooleanField(default=False, blank=True, null=True, verbose_name="Trabalha?")
    where_works = models.CharField(max_length=100, blank=True, null=True, verbose_name="Onde trabalha")
    already_worked = models.BooleanField(default=False, blank=True, null=True, verbose_name="Já trabalhou")
    where_worked = models.CharField(max_length=100, blank=True, null=True, verbose_name="Onde trabalhou")
    interests = models.CharField(max_length=100, blank=True, null=True, verbose_name="Quais são seus interesses")
    makes_track = models.BooleanField(default=False, blank=True, null=True, verbose_name="Faz pista?")
    track_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo de pista")
    where_makes_track = models.CharField(max_length=100, blank=True, null=True, verbose_name="Onde faz pista")
    documents_owned = models.CharField(max_length=100, blank=True, null=True, verbose_name="Quais documentos possui")
    rectified_name_and_gender = models.BooleanField(default=False, blank=True, null=True,
                                                    verbose_name="Nome e gênero retificados?")
    willing_to_rectify = models.BooleanField(default=False, blank=True, null=True, verbose_name="Deseja retificar?")
    been_arrested = models.BooleanField(default=False, blank=True, null=True, verbose_name="Já foi presa?")
    city_arrested = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade em que foi  presa")
    year_arrested = models.CharField(max_length=20, blank=True, null=True, verbose_name="Ano da prisão")
    was_processed = models.BooleanField(default=False, blank=True, null=True, verbose_name="Tem processo")

    def __str__(self):
        return f'Ficha N°{self.id}'

    class Meta:
        verbose_name = "Ficha Transpasse"
        verbose_name_plural = "Fichas Transpasse"

    def get_pessoas(self):
        return self.assisted_person.full_name


class AtendimentoDRS(models.Model):
    assisted_person = models.ForeignKey('Pessoa',  on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name="atendimento_drs", verbose_name="Pessoa assistida")
    how_knew_about_drs = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Como soube do DRS"))
    current_occupation = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Ocupação atual"))
    had_other_occupations = models.CharField(max_length=100, blank=True, null=True,
                                             verbose_name=_("Teve outros trabalhos"))
    relevant_information = models.TextField(max_length=900, blank=True, null=True,
                                            verbose_name="Informações relevantes",
                                            help_text="exemplos: uso de drogas, trajetória/situação de rua, "
                                                      "violência doméstica, abuso sexual")
    reference_entities = models.OneToOneField(Entidade, blank=True, null=True, verbose_name="Entidade de referência",
                                              on_delete=models.SET_NULL)
    follow_up_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo de acompanhamento")
    last_attendance_date = models.DateField(blank=True, null=True, verbose_name='Último atendimento/visita')

    class Meta:
        verbose_name = "Ficha DRS"
        verbose_name_plural = "Fichas DRS"

    def get_pessoas(self):
        return self.assisted_person.full_name


class AcompanhamentoTranspasse(models.Model):
    comments = models.TextField(max_length=2000, default='', verbose_name="Observações",
                                help_text="Tarefas/Acompanhamentos/Atendimentos")
    atendimento_transpasse = models.ForeignKey(AtendimentoTranspasse, on_delete=models.CASCADE)


class AcompanhamentoDRS(models.Model):
    comments = models.TextField(max_length=2000, default='', verbose_name="Observações",
                                help_text="Tarefas/Acompanhamentos/Atendimentos")
    atendimento_drs = models.ForeignKey(AtendimentoDRS, on_delete=models.CASCADE)



