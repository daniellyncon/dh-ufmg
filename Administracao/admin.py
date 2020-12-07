from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)


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
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('last_login',)
    list_display = ('get_name', 'get_bond_type', 'email', 'get_phone', 'get_axis')
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

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False
        return request.user.is_superuser or request.user.id == obj.id

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("get_responsibles", "title", "deadline", "is_done")
    list_filter = ("deadline", "responsible", "is_done")
    autocomplete_fields = ()
    search_fields = ("title",)
    readonly_fields = ("id",)
    fieldsets = (
        (None, {"fields": ("title", "deadline", "description", "responsible", "is_done")}),
    )

    def get_responsibles(self, obj):
        return ", ".join([e.perfil.name for e in obj.responsible.all()])

    get_responsibles.short_description = "Reponsáveis"

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


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

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    list_display = ("name", "reference_person", "reference_person_contact", "eixos")
    list_filter = ("axis",)
    autocomplete_fields = ()
    search_fields = ("name", "reference_person")
    fieldsets = (
        ("Dados da entidade", {"fields": ("name", "entity_liked", "description", "contact", "comments",
                                          "person", 'axis')}),
        ("Endereço da entidade", {"fields": ("street", "number", "complement",
                                             "neighborhood", "city", "state",)}),
        ("Dados pessoa de referência", {"fields": ("reference_person", "reference_person_contact",
                                                   "reference_function", "reference_profission", "reference_sector")})
    )

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("type", "date", "link")

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "source")

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
