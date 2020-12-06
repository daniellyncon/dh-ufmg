# Generated by Django 3.1.3 on 2020-12-06 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Administracao', '0005_auto_20201204_2313'),
        ('Atendimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recurso',
            options={'verbose_name': 'Recurso', 'verbose_name_plural': 'Recursos'},
        ),
        migrations.RemoveField(
            model_name='atendimentodrs',
            name='axis',
        ),
        migrations.RemoveField(
            model_name='atendimentotranspasse',
            name='axis',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='axis',
            field=models.ManyToManyField(to='Administracao.Eixo', verbose_name='Eixos relacionados'),
        ),
        migrations.AlterField(
            model_name='atendimentodrs',
            name='assisted_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atendimento_drs', to='Atendimento.pessoa', verbose_name='Pessoa assistida'),
        ),
        migrations.AlterField(
            model_name='atendimentodrs',
            name='last_attendance_date',
            field=models.DateField(blank=True, null=True, verbose_name='Último atendimento/visita'),
        ),
        migrations.AlterField(
            model_name='atendimentotranspasse',
            name='ist_exams_up_to_date',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Exames IST em dia'),
        ),
        migrations.AlterField(
            model_name='atendimentotranspasse',
            name='psychology_intern',
            field=models.ForeignKey(blank=True, limit_choices_to={'Estagiario': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Estagiária de psicologia responsável'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='birth_state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado de nascimento'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='gender_identity',
            field=models.CharField(blank=True, choices=[('1', 'Agênero'), ('2', 'Cisgênero'), ('3', 'Gênero flúido'), ('4', 'Transgênero'), ('5', 'Crossdresser'), ('6', 'Drag Queen'), ('7', 'Não-binário')], max_length=50, null=True, verbose_name='Identidade de gênero'),
        ),
    ]
