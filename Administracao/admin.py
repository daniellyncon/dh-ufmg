from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.admin import UserAdmin
from .models import *


class TarefaDocumentoInline(admin.StackedInline):
    model = Documento.tasks.through
    extra = 0
    verbose_name = "Documento relacionado"


class TarefaInline(admin.StackedInline):
    model = Tarefa
    extra = 1
    # readonly_fields = ("id", "duration")
    fields = (
        "title",
    )


class PlantaoInline(admin.StackedInline):
    model = Plantao
    extra = 1
    verbose_name = "Plantão"
    verbose_name_plural = 'Plantões'
    min_num = 1
    can_delete = True
    show_change_link = True
    fields = (
        "day_of_the_week", "start_time", "end_time"
    )


class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 1
    fields = (
        'street', 'number', 'complement', 'neighborhood', 'city', 'state'
    )
    verbose_name = 'Endereço'
    verbose_name_plural = 'Endereço'


class ProfileInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'user'


@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, EnderecoInline, PlantaoInline)
    fieldsets = (
        (None, {'fields': ('email', 'last_login', 'date_joined', 'is_active')}),
        # (_('Permissions'), {
        #     'fields': ('is_active', 'groups', 'user_permissions'),
        # }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('last_login',)
    list_display = ('get_name', 'get_bond_type', 'email', 'get_phone', 'get_axis')
    # list_display_links = ('get_axis',)
    list_filter = ('is_superuser', 'is_active', 'perfil__axis')
    search_fields = ("get_name", 'email',)
    ordering = ()
    filter_horizontal = ('groups', 'user_permissions',)

    def get_name(self, obj):
        return obj.perfil.name

    def get_bond_type(self, obj):
        return obj.perfil.get_bond_type_display()

    def get_axis(self, obj):
        return obj.perfil.get_axis()

    get_name.admin_order_field = 'perfil'  # Allows column order sorting
    get_name.short_description = 'Nome'  # Renames column head
    get_bond_type.short_description = 'Tipo de vínculo'
    get_bond_type.admin_order_field = 'bond_type'
    get_axis.short_description = 'Eixo'
    Usuario.get_phone.short_description = 'Telefone'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("get_responsibles", "title", "deadline", "is_done")
    list_filter = ("deadline", "responsible", "is_done")
    autocomplete_fields = ()
    search_fields = ("title",)
    # inlines = [TarefaDocumentoInline, ]
    readonly_fields = ("id",)
    fieldsets = (
        (None, {"fields": ("title", "deadline", "description", "responsible", "is_done")}),
    )

    def get_responsibles(self, obj):
        return ", ".join([e.perfil.name for e in obj.responsible.all()])

    get_responsibles.short_description = "Reponsáveis"


@admin.register(Eixo)
class EixoAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    list_filter = ("name",)
    autocomplete_fields = ()
    search_fields = ("name",)
    readonly_fields = ("id",)
    fieldsets = (
        (None, {"fields": ("name",)}),
    )


@admin.register(Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    list_display = ("name", "reference_person", "reference_person_contact", "eixos")
    list_filter = ("axis",)
    autocomplete_fields = ()
    search_fields = ("name", "reference_person")
    readonly_fields = ("id",)
    fieldsets = (
        ("Dados da entidade", {"fields": ("name", "entity_liked", "description", "contact", "comments",
                                          "person", 'axis')}),
        ("Endereço da entidade", {"fields": ("street", "number", "complement",
                                             "neighborhood", "city", "state",)}),
        ("Dados pessoa de referência", {"fields": ("reference_person", "reference_person_contact",
                                                   "reference_function", "reference_profission", "reference_sector")})
    )


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("type", "date", "link")


@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "source")


# class TaskAdminForm(forms.ModelForm):
#     fields = ["title", "deadline", "description", "responsible", "is_done"]
#     exclude = ()
#     documents = forms.ModelMultipleChoiceField(
#         queryset=Documento.objects.all(),
#         required=False,
#         widget=FilteredSelectMultiple(
#             verbose_name='Documentos relacionados',
#             is_stacked=False
#         )
#     )
#
#     class Meta:
#         model = Tarefa
#
#     def __init__(self, *args, **kwargs):
#         super(TaskAdminForm, self).__init__(*args, **kwargs)
#
#         if self.instance and self.instance.pk:
#             self.fields['documents'].initial = self.instance.pizzas.all()
#
#     def save(self, commit=True):
#         task = super(TaskAdminForm, self).save(commit=False)
#
#         if commit:
#             task.save()
#
#         if task.pk:
#             task.documents = self.cleaned_data['documents']
#             self.save_m2m()
#
#         return task
