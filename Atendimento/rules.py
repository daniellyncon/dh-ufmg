from .models import Pessoa, Processo, Eixo


TRANSPASSE = Eixo.objects.filter(name__icontains='transpasse').get()
DRS = Eixo.objects.filter(name__icontains='drs').get()


def is_same_axis(user, obj):
    user_axis = user.axis.all()
    obj_axis = obj.axis.all()
    return any(axis in user_axis for axis in obj_axis)


def filter_by_axis(user, queryset):
    user_axis = user.axis.all()
    return queryset.filter(axis__in=user_axis)


def relation_processo_pessoa(user, queryset):
    pessoas = filter_by_axis(user, Pessoa.objects.all())
    return queryset.filter(related_people__in=pessoas)


def relation_recurso_processo(user, queryset):
    processos = relation_processo_pessoa(user, Processo.objects.all())
    return queryset.filter(law_suit__in=processos)


def is_transpasse(user):
    return TRANSPASSE in user.axis.all()


def is_drs(user):
    return DRS in user.axis.all()
