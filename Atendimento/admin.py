# from django import forms
from django.contrib import admin
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from Administracao.admin import EnderecoInline
from Administracao.widgets import CustomDateInput
from .models import *
from django.db import models


class RecursoInline(admin.StackedInline):
    model = Recurso
    # readonly_fields = ("pk", )
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


class RecursoHistoricoInline(admin.StackedInline):
    model = HistoricoRecurso
    fields = (
        'judicial_appeal', 'date', 'description',
    )
    extra = 1
    can_delete = True
    show_change_link = True


@admin.register(Caso)
class CasoAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_areas', 'daj_number')
    fieldsets = (
        ("Dados do caso", {"fields": ('related_areas', 'daj_number', 'daj_advisor', 'daj_intern',
                                      'registration_date', 'solution_date',
                                      'advisor', 'intern', 'assisted_person',
                                      'law_suits', 'entities', 'axis', 'tasks', 'documents')}),
    )
    list_display_links = ()
    # list_filter = ("author", "genre")
    list_select_related = False
    list_per_page = 20
    list_max_show_all = 100
    # list_editable = ("title",)
    search_fields = ("law_suit_number",)
    # autocomplete_fields = ("genre",)
    # date_hierarchy = "published_on"
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = ()
    actions = []
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True


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
    # list_editable = ("title",)
    search_fields = ("law_suit_number",)
    # autocomplete_fields = ("genre",)
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

    formfield_overrides = {
        models.DateField: {'widget': CustomDateInput},
    }

    Processo.get_law_area.short_description = 'Área do direito'
    Processo.get_recursos.short_description = 'Recursos relacionados'
    Processo.get_pessoas.short_description = 'Pessoas relacionadas'


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('type', 'judicial_appeal_number')
    fieldsets = (
        ("Dados do recurso", {"fields": ('law_suit', 'type', 'judicial_appeal_number', 'plenary', 'report', 'resume')}),
    )
    list_display_links = ()
    # list_filter = ("author", "genre")
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
        ("Dados Pessoais", {"fields": ('first_appointment_date', 'full_name', 'civil_registry', 'rg', 'cpf', 'get_age',
                                       'birth_city', 'birth_state', 'phone', 'birthday', 'mother_name', 'civil_status',
                                       'gender_identity', 'preferred_pronouns', 'self_identification', 'schooling')}),
        ("Saúde", {"fields": ("has_health_problem", "which_health_problem", "receives_assistance", "which_assistance",
                              )}),
        ("Contato", {"fields": ("related_person", "related_person_bond", "contact_email", "contact_phone",
                                )}),
    )
    # raw_id_fields = ("author",)
    readonly_fields = ("get_age",)
    # list_display_links = ()
    # list_filter = ("author", "genre")
    # list_select_related = False
    list_per_page = 20
    list_max_show_all = 100
    # list_editable = ("title",)
    search_fields = ("full_name",)
    # autocomplete_fields = ("genre",)
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

    formfield_overrides = {
        models.DateField: {'widget': CustomDateInput},
    }

    def get_age(self, obj):
        if obj.birthday:
            today = datetime.date.today()
            return today.year - obj.birthday.year - (
                    (today.month, today.day) < (obj.birthday.month, obj.birthday.day)
            )
        else:
            return ''

    get_age.short_description = 'Idade'


@admin.register(AtendimentoDRS)
class DrsAdmin(admin.ModelAdmin):
    list_display = ('get_pessoas',)
    fieldsets = (
        ("Atendimento DRS", {"fields": ('assisted_person', 'how_knew_about_drs', 'current_occupation',
                                        'had_other_occupations', 'relevant_information', 'reference_entities',
                                        'follow_up_type', 'last_attendance_date',)}),
    )
    autocomplete_fields = ('assisted_person',)
    list_display_links = ('get_pessoas',)
    # list_filter = ("author", "genre")
    list_select_related = True
    list_per_page = 20
    list_max_show_all = 100
    # list_editable = ("title",)
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


@admin.register(AtendimentoTranspasse)
class TranpasseAdmin(admin.ModelAdmin):
    list_display = ('get_pessoas',)
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
    autocomplete_fields = ('assisted_person',)
    list_display_links = ('get_pessoas',)
    # list_filter = ("author", "genre")
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
