from datetime import date

from django.contrib import admin
from Administracao.admin import EnderecoInline
from .rules import is_same_axis, filter_by_axis, relation_processo_pessoa, relation_recurso_processo, is_drs, \
    is_transpasse
from .models import *


class RecursoInline(admin.StackedInline):
    model = Recurso
    fields = (
        'type', 'judicial_appeal_number', 'plenary', 'report', 'resume'
    )
    extra = 1
    verbose_name = 'Recurso'
    verbose_name_plural = 'Recursos'
    can_delete = True
    show_change_link = True


class AcompanhamentoDRSInline(admin.StackedInline):
    model = AcompanhamentoDRS
    fields = ('comments',)
    extra = 1
    verbose_name = 'Acompanhamento'
    verbose_name_plural = 'Acompanhamentos'
    can_delete = True
    show_change_link = True


class AcompanhamentoTranspasseInline(admin.StackedInline):
    model = AcompanhamentoTranspasse
    fields = ('comments',)
    extra = 1
    verbose_name = 'Acompanhamento'
    verbose_name_plural = 'Acompanhamentos'
    can_delete = True
    show_change_link = True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request, obj):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class AtendimentoTranspasseInline(admin.StackedInline):
    model = AtendimentoTranspasse
    fields = ('assisted_person', 'how_knew_about_transpasse', 'psychology_intern', 'lives_with', 'cities_lived',
              'ist_exams_up_to_date', 'last_time_been_health_center', 'is_drug_user', 'which_drugs',
              'consider_drugs_bad', 'uses_hormones', 'use_accompanied_by_doctor', 'which_hormones', 'works',
              'where_works', 'already_worked', 'where_worked', 'interests', 'makes_track', 'track_type',
              'where_makes_track', 'documents_owned', 'rectified_name_and_gender', 'willing_to_rectify',
              'been_arrested', 'city_arrested', 'year_arrested', 'was_processed')
    extra = 1
    verbose_name = 'Ficha Transpasse'
    verbose_name_plural = 'Fichas Transpasse'
    can_delete = True
    show_change_link = True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request, obj):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class AtendimentoDRSInline(admin.StackedInline):
    model = AtendimentoDRS
    fields = ('assisted_person', 'how_knew_about_drs', 'current_occupation',
              'had_other_occupations', 'relevant_information', 'reference_entities',
              'follow_up_type', 'last_attendance_date',)
    extra = 1
    verbose_name = 'Ficha DRS'
    verbose_name_plural = 'Fichas DRS'
    can_delete = True
    show_change_link = True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request, obj):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class RecursoHistoricoInline(admin.StackedInline):
    model = HistoricoRecurso
    fields = (
        'judicial_appeal', 'date', 'description',
    )
    extra = 1
    can_delete = True
    show_change_link = True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request, obj):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class ObservacoesCasoInline(admin.StackedInline):
    model = ObservacoesCaso
    extra = 1
    can_delete = True
    show_change_link = True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request, obj):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class ObservacoesPessoaInline(admin.StackedInline):
    model = ObservacoesPessoa
    extra = 1
    can_delete = True
    show_change_link = True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request, obj):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class ObservacoesProcessoInline(admin.StackedInline):
    model = ObservacoesProcesso
    extra = 1
    can_delete = True
    show_change_link = True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request, obj):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Caso)
class CasoAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_areas', 'daj_number')
    fieldsets = (
        ("Dados do caso", {"fields": ('related_areas', 'reference_contacts', 'daj_number', 'daj_advisor', 'daj_intern',
                                      'registration_date', 'solution_date', 'advisor', 'intern', 'assisted_person',
                                      'is_active', 'is_amicus_curiae', 'report',  'law_suits', 'entities', 'axis',
                                      'tasks', 'documents')}),
    )
    list_filter = ('is_active', )
    list_display_links = ()
    list_select_related = False
    list_per_page = 20
    list_max_show_all = 100
    search_fields = ("law_suit_number",)
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = (ObservacoesCasoInline, )
    actions = []
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_same_axis(request.user, obj)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_same_axis(request.user, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_same_axis(request.user, obj)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return filter_by_axis(request.user, queryset)


@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    list_display = ('law_suit_number', 'get_law_area', 'get_recursos', 'get_pessoas')
    fieldsets = (
        ("Dados do processo", {"fields": ('law_suit_number', 'action_type', 'open_mandate', 'district', 'law_area',
                                          'latest_moves', 'has_lawyer', 'lawyer_name', 'lawyer_contact',
                                          'followed_by_daj', 'minhadaj_number', 'start_date', 'transit_date',
                                          'related_people',)}),
    )
    list_display_links = ()
    list_filter = ("law_area",)
    list_select_related = True
    list_per_page = 20
    list_max_show_all = 100
    search_fields = ("law_suit_number",)
    date_hierarchy = "start_date"
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = (RecursoInline,)
    actions = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

    Processo.get_law_area.short_description = 'Área do direito'
    Processo.get_recursos.short_description = 'Recursos relacionados'
    Processo.get_pessoas.short_description = 'Pessoas relacionadas'

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj in relation_processo_pessoa(request.user, Processo.objects.all())

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj in relation_processo_pessoa(request.user, Processo.objects.all())

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj in relation_processo_pessoa(request.user, Processo.objects.all())

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return relation_processo_pessoa(request.user, queryset)


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('type', 'judicial_appeal_number')
    fieldsets = (
        ("Dados do recurso", {"fields": ('law_suit', 'type', 'judicial_appeal_number', 'plenary', 'report', 'resume',
                                         'transit_date')}),
    )
    list_display_links = ()
    list_select_related = True
    list_per_page = 20
    list_max_show_all = 100
    search_fields = ("type",)
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = (RecursoHistoricoInline,)
    actions = []
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj in relation_recurso_processo(request.user, Recurso.objects.all())

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj in relation_recurso_processo(request.user, Recurso.objects.all())

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj in relation_recurso_processo(request.user, Recurso.objects.all())

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return relation_recurso_processo(request.user, queryset)


class PessoaInline(admin.StackedInline):
    model = Pessoa
    extra = 1
    readonly_fields = ("id", "duration")
    fields = (
        "assisted", "full_name",
    )


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'get_related_cases')
    fieldsets = (
        ("Dados Pessoais", {"fields": ('assisted', 'responsible_advisor', 'responsible_intern',
                                       'first_appointment_date', 'full_name', 'civil_registry', 'rg', 'cpf', 'cnh',
                                       'get_age', 'birth_city', 'birth_state', 'phone', 'birthday', 'mother_name',
                                       'civil_status', 'gender_identity', 'preferred_pronouns', 'self_identification',
                                       'schooling', "axis")}),
        ("Saúde", {"fields": ("has_health_problem", "which_health_problem", "receives_assistance", "which_assistance",
                              )}),
        ("Contato", {"fields": ("related_person", "related_person_bond", "contact_email", "contact_phone",

                                'reference_regional_administration', "street", "number", "complement", "neighborhood",
                                "city", "state")}),
    )
    readonly_fields = ("get_age",)
    list_per_page = 20
    list_max_show_all = 100
    search_fields = ("full_name",)
    list_select_related = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = (EnderecoInline, AtendimentoTranspasseInline, AtendimentoDRSInline)
    actions = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

    def get_age(self, obj):
        if obj.birthday:
            today = date.today()
            return today.year - obj.birthday.year - (
                    (today.month, today.day) < (obj.birthday.month, obj.birthday.day)
            )
        else:
            return ''

    get_age.short_description = 'Idade'

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_same_axis(request.user, obj)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_same_axis(request.user, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_same_axis(request.user, obj)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return filter_by_axis(request.user, queryset)


@admin.register(AtendimentoDRS)
class DrsAdmin(admin.ModelAdmin):
    list_display = ('assisted_person', 'id')
    fieldsets = (
        ("Atendimento DRS", {"fields": ('assisted_person', 'how_knew_about_drs', 'current_occupation',
                                        'had_other_occupations', 'relevant_information', 'reference_entities',
                                        'follow_up_type', 'last_attendance_date',)}),
    )
    autocomplete_fields = ('assisted_person',)
    list_display_links = ('assisted_person',)
    list_select_related = True
    list_per_page = 20
    list_max_show_all = 100
    search_fields = ("assisted_person",)
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = (AcompanhamentoDRSInline,)
    actions = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

    def has_module_permission(self, request):
        return request.user.is_superuser or is_drs(request.user)

    def has_add_permission(self, request):
        return request.user.is_superuser or is_drs(request.user)

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_drs(request.user)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_drs(request.user)

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_drs(request.user)


@admin.register(AtendimentoTranspasse)
class TranpasseAdmin(admin.ModelAdmin):
    list_display = ('assisted_person', 'id')
    fieldsets = (
        ("Transpasse", {"fields": ('assisted_person', 'how_knew_about_transpasse', 'psychology_intern',
                                   'lives_with', 'cities_lived', 'ist_exams_up_to_date',
                                   'last_time_been_health_center', 'is_drug_user', 'which_drugs',
                                   'consider_drugs_bad', 'uses_hormones', 'use_accompanied_by_doctor',
                                   'which_hormones', 'works', 'where_works', 'already_worked', 'where_worked',
                                   'interests', 'makes_track', 'track_type', 'where_makes_track',
                                   'documents_owned', 'rectified_name_and_gender', 'willing_to_rectify',
                                   'been_arrested', 'city_arrested', 'year_arrested', 'was_processed')}),
    )
    autocomplete_fields = ('assisted_person', )
    list_display_links = ('assisted_person', )
    list_select_related = True
    list_per_page = 20
    list_max_show_all = 100
    search_fields = ("assisted_person",)
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = (AcompanhamentoTranspasseInline,)
    actions = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

    def has_module_permission(self, request):
        return request.user.is_superuser or is_transpasse(request.user)

    def has_add_permission(self, request):
        return request.user.is_superuser or is_transpasse(request.user)

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_transpasse(request.user)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_transpasse(request.user)

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or is_transpasse(request.user)
