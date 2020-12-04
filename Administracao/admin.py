from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import Eixo, Tarefa, Documento, Entidade, Endereco, Plantao, Perfil, Usuario, Frase
from django.contrib.auth.models import Group
from .widgets import CustomDateInput
from django.db import models


admin.site.unregister(Group)


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
    fields = (
        "day_of_the_week", "start_time", "end_time"
    )


class EnderecoInline(InlineModelAdmin):
    model = Endereco
    extra = 1
    # readonly_fields = ("id", "duration")
    fields = (
        'street', 'number', 'complement', 'neighborhood', 'city', 'state'
    )


class ProfileInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfis'
    fk_name = 'user'
    formfield_overrides = {
        models.DateField: {'widget': CustomDateInput},
    }


@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    formfield_overrides = {
        models.DateField: {'widget': CustomDateInput},
    }
    list_display = ('get_name', 'get_bond_type', 'email', 'get_axis')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'perfil__axis')
    search_fields = ('email', )
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    def get_name(self, obj):
        return obj.perfil.name

    def get_bond_type(self, obj):
        return obj.perfil.bond_type

    def get_axis(self, obj):
        return obj.profile.axis.name

    get_name.admin_order_field = 'perfil'  # Allows column order sorting
    get_name.short_description = 'Nome'  # Renames column head
    get_bond_type.short_description = 'Tipo de vínculo'
    get_bond_type.admin_order_field = 'bond_type'
    get_axis.short_description = 'Eixo'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("title", "id")
    list_filter = ("deadline", "responsible", "is_done")
    autocomplete_fields = ()
    search_fields = ("title",)
    readonly_fields = ("id",)
    fieldsets = (
        (None, {"fields": ("title", "deadline", "description", "responsible", "is_done")}),
        # ("SegundaTab", {"fields": ()}),
    )
    formfield_overrides = {
        models.DateField: {'widget': CustomDateInput},
    }


@admin.register(Eixo)
class EixoAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    list_filter = ("name",)
    autocomplete_fields = ()
    search_fields = ("name",)
    readonly_fields = ("id",)
    fieldsets = (
        (None, {"fields": ("name", )}),
        # ("SegundaTab", {"fields": ()}),
    )



@admin.register(Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    list_display = ("name", "reference_person", "reference_person_contact", "eixos")
    list_filter = ("axis",)
    autocomplete_fields = ()
    search_fields = ("name", "reference_person")
    readonly_fields = ("id",)
    fieldsets = (
        ("Dados da entidade", {"fields": ("name", "entity_liked", "description", "contact", "reference_person",
                                          "reference_person_contact", "comments", "person", 'axis')}),
        ("Endereço da entidade", {"fields": ("street", "number", "complement", "neighborhood", "city", "state",)}),
    )
    formfield_overrides = {
        models.DateField: {'widget': CustomDateInput},
    }


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("type", "date", "link")
    formfield_overrides = {
        models.DateField: {'widget': CustomDateInput(format='%dd/%mm/%YYYY')},
    }


@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "source")
