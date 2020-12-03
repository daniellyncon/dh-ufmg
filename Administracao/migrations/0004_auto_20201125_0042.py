# Generated by Django 3.1.3 on 2020-11-25 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracao', '0003_auto_20201124_1837'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'verbose_name_plural': 'Perfis'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'Usuários'},
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='on_duty',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='axis',
        ),
        migrations.AddField(
            model_name='perfil',
            name='axis',
            field=models.ManyToManyField(related_name='eixo', to='Administracao.Eixo', verbose_name='Eixo'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='bond_type',
            field=models.CharField(blank=True, choices=[('1', 'Coordenador'), ('2', 'Orientador'), ('3', 'Estagiário'), ('4', 'Colaborador Eventual')], max_length=50, null=True, verbose_name='Tipo de vínculo'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='cnh',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='CNH'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='course',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='date_fired',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Data de desligamento'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='registration',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nº de matrícula'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='rg',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='RG'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='scholarship',
            field=models.CharField(blank=True, choices=[('1', 'Bolsista'), ('2', 'Voluntário')], max_length=50, null=True, verbose_name='Bolsista'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='scholarship_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de bolsa'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='university',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Universidade'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Administracao.endereco'),
        ),
        migrations.AlterField(
            model_name='plantao',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
