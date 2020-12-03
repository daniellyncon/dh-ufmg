# Generated by Django 3.1.3 on 2020-12-03 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracao', '0006_auto_20201203_1730'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Atendimento', '0002_auto_20201125_0042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atendimentodrs',
            options={'verbose_name': 'Ficha DRS', 'verbose_name_plural': 'Fichas DRS'},
        ),
        migrations.AlterModelOptions(
            name='atendimentotranspasse',
            options={'verbose_name': 'Ficha Transpasse', 'verbose_name_plural': 'Fichas Transpasse'},
        ),
        migrations.AddField(
            model_name='atendimentodrs',
            name='assisted_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atendimento_drs', to='Atendimento.pessoa'),
        ),
        migrations.AddField(
            model_name='atendimentodrs',
            name='axis',
            field=models.ManyToManyField(to='Administracao.Eixo', verbose_name='Eixos relacionados'),
        ),
        migrations.AddField(
            model_name='atendimentodrs',
            name='current_occupation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ocupação atual'),
        ),
        migrations.AddField(
            model_name='atendimentodrs',
            name='follow_up_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tipo de acompanhamento'),
        ),
        migrations.AddField(
            model_name='atendimentodrs',
            name='had_other_occupations',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Teve outros trabalhos'),
        ),
        migrations.AddField(
            model_name='atendimentodrs',
            name='how_knew_about_drs',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Como soube do DRS'),
        ),
        migrations.AddField(
            model_name='atendimentodrs',
            name='last_attendance_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='atendimentodrs',
            name='reference_entities',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Administracao.entidade', verbose_name='Entidade de referência'),
        ),
        migrations.AddField(
            model_name='atendimentodrs',
            name='relevant_information',
            field=models.TextField(blank=True, help_text='exemplos: uso de drogas, trajetória/situação de rua, violência doméstica, abuso sexual', max_length=900, null=True, verbose_name='Informações relevantes'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='already_worked',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Já trabalhou'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='assisted_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atendimento_transpasse', to='Atendimento.pessoa'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='axis',
            field=models.ManyToManyField(to='Administracao.Eixo', verbose_name='Eixos relacionados'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='been_arrested',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Já foi presa?'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='cities_lived',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidades por onde passou'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='city_arrested',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade em que foi  presa'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='consider_drugs_bad',
            field=models.BooleanField(default=False, verbose_name='Considera o uso prejudicial'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='documents_owned',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Quais documentos possui'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='how_knew_about_transpasse',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Como soube do Transpasse'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='interests',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Quais são seus interesses'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='is_drug_user',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Faz uso de álcool e drogas'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='ist_exams_up_to_date',
            field=models.BooleanField(default=False, verbose_name='Exames IST em dia'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='last_time_been_health_center',
            field=models.CharField(blank=True, choices=[('1', 'Vou com frequência'), ('2', '1 a 3 meses atrás'), ('3', '3 a 6 meses atrás'), ('4', 'Mais de 6 meses'), ('5', 'Mais de um ano')], max_length=100, null=True, verbose_name='Última vez que foi ao posto de saúde'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='lives_with',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Com quem mora'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='makes_track',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Faz pista?'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='psychology_intern',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Estagiária de psicologia responsável'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='rectified_name_and_gender',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Nome e gênero retificados?'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='track_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tipo de pista'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='use_accompanied_by_doctor',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Uso acompanhado por médico'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='uses_hormones',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Faz uso de hormônios'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='was_processed',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Tem processo'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='where_makes_track',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Onde faz pista'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='where_worked',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Onde trabalhou'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='where_works',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Onde trabalha'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='which_drugs',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Quais drogas usa'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='which_hormones',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Qual(is) hormônios'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='willing_to_rectify',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Deseja retificar?'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='works',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Trabalha?'),
        ),
        migrations.AddField(
            model_name='atendimentotranspasse',
            name='year_arrested',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Ano da prisão'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='related_case_bond',
            field=models.CharField(blank=True, choices=[('1', 'Assistido'), ('2', 'Jurisdicionado'), ('3', 'Atingido'), ('4', 'Terceiro'), ('5', 'Interessado'), ('6', 'Outro')], max_length=30, null=True, verbose_name='Vínculo caso'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='related_law_suit_bond',
            field=models.CharField(blank=True, choices=[('1', 'Parte autora'), ('2', 'Parte ré'), ('3', 'Terceiro'), ('4', 'interessado')], max_length=50, null=True, verbose_name='Vínculo processo'),
        ),
        migrations.CreateModel(
            name='AcompanhamentoTranspasse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(default='', help_text='Tarefas/Acompanhamentos/Atendimentos', max_length=2000, verbose_name='Observações')),
                ('atendimento_transpasse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atendimento.atendimentotranspasse')),
            ],
        ),
        migrations.CreateModel(
            name='AcompanhamentoDRS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(default='', help_text='Tarefas/Acompanhamentos/Atendimentos', max_length=2000, verbose_name='Observações')),
                ('atendimento_drs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atendimento.atendimentodrs')),
            ],
        ),
    ]
