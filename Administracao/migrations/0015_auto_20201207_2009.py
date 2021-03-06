# Generated by Django 3.1.3 on 2020-12-07 23:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Administracao', '0014_auto_20201207_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='produção/recebimento/envio/protocolo', verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='deadline',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Prazo'),
        ),
    ]
