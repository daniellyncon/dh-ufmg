# Generated by Django 3.1 on 2020-10-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('on_duty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onduty',
            name='day_of_the_week',
            field=models.CharField(blank=True, choices=[('1', 'Segunda-feira'), ('2', 'Terça-feira'), ('3', 'Quarta-feira'), ('4', 'Quinta-feira'), ('5', 'Sexta-feira')], max_length=10, null=True, verbose_name='Dia da semana'),
        ),
    ]
