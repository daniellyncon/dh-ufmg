# Generated by Django 3.1 on 2020-09-24 04:12

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('axis', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnDuty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_the_week', models.IntegerField(verbose_name='Dia da semana')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('username', models.CharField(blank=True, default=None, max_length=1, null=True)),
                ('first_name', models.CharField(blank=True, default=None, max_length=1, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=1, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('bond_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de vínculo')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('registration', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nº de matrícula')),
                ('street_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua')),
                ('number_address', models.IntegerField(blank=True, null=True, verbose_name='Número')),
                ('complement_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('neighborhood_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('city_address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cidade')),
                ('state_address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado')),
                ('course', models.CharField(blank=True, max_length=50, null=True, verbose_name='Curso')),
                ('university', models.CharField(blank=True, max_length=50, null=True, verbose_name='Universidade')),
                ('department', models.CharField(blank=True, max_length=50, null=True, verbose_name='Departamento')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('cpf', models.CharField(max_length=50, verbose_name='CPF')),
                ('cnh', models.CharField(blank=True, max_length=50, null=True, verbose_name='CNH')),
                ('date_joined', models.DateField(verbose_name='Data de entrada na CDH')),
                ('date_fired', models.DateField(verbose_name='Data de desligamento')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('scholarship', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bolsista')),
                ('scholarship_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de bolsa')),
                ('axis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='axis.axis', verbose_name='Eixo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('on_duty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.onduty', verbose_name='Plantão')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
