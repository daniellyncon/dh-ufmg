import datetime

from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from Administracao.admin import EnderecoInline
from .models import Caso, Processo, Recurso, HistoricoRecurso, Pessoa, AtendimentoTranspasse, AtendimentoDRS


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


class RecursoHistoricoInline(admin.StackedInline):
    model = HistoricoRecurso
    readonly_fields = ("id", )
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
        ("Dados do processo", {"fields": ('related_areas', 'daj_number', 'daj_advisor', 'daj_intern',
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
    search_fields = ("law_suit_number", )
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
    list_display = ('law_suit_number', 'law_area', 'law_area')
    fieldsets = (
        ("Dados do processo", {"fields": ('law_suit_number', 'action_type', 'open_mandate', 'district', 'law_area',
                                          'latest_moves', 'has_lawyer', 'lawyer_name', 'lawyer_contact',
                                          'followed_by_daj', 'minhadaj_number', 'start_date', 'transit_date',
                                          'related_people', )}),
    )
    list_display_links = ()
    # list_filter = ("author", "genre")
    list_select_related = False
    list_per_page = 20
    list_max_show_all = 100
    # list_editable = ("title",)
    search_fields = ("law_suit_number", )
    # autocomplete_fields = ("genre",)
    # date_hierarchy = "published_on"
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = (RecursoInline, )
    actions = []
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('type', 'judicial_appeal_number')
    fieldsets = (
        ("Dados do recurso", {"fields": ('type', 'judicial_appeal_number', 'plenary', 'report', 'resume')}),
    )
    list_display_links = ()
    # list_filter = ("author", "genre")
    list_select_related = False
    list_per_page = 20
    list_max_show_all = 100
    search_fields = ("type", )
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = (RecursoHistoricoInline, )
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
    list_display = ('full_name', 'phone', )
    fieldsets = (
        ("Identificação", {"fields": ('first_appointment_date', 'full_name', 'civil_registry', 'rg', 'cpf',
                                      'birth_city', 'birth_state', 'phone', 'contact_phone', 'birthday',
                                      'mother_name', 'civil_status', 'gender_identity',
                                      'preferred_pronouns', 'self_identification', 'schooling')}),
        # ("Saúde", {"fields": ("genre", "summary", "isbn", "published_on")}),
    )
    # raw_id_fields = ("author",)
    # readonly_fields = ("get_age",)
    list_display_links = ()
    # list_filter = ("author", "genre")
    list_select_related = False
    list_per_page = 20
    list_max_show_all = 100
    # list_editable = ("title",)
    search_fields = ("full_name", )
    # autocomplete_fields = ("genre",)
    # date_hierarchy = "published_on"
    save_as = True
    save_as_continue = True
    save_on_top = True
    preserve_filters = True
    inlines = (EnderecoInline,)
    actions = []
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True

    def get_age(self, kwargs):
        if self.birthday:
            today = datetime.date.today()
            return today.year - self.birthday.year - (
                    (today.month, today.day) < (self.birthday.month, self.birthday.day)
            )
        else:
            return ''
