# Generated by Django 3.1 on 2020-10-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_remove_person_related_law_suit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='related_case_bond',
            field=models.CharField(blank=True, choices=[('1', 'assistido'), ('2', 'jurisdicionado'), ('3', 'atingido'), ('4', 'terceiro'), ('5', 'interessado'), ('6', 'outro'), ('7', 'test')], max_length=30, null=True, verbose_name='Vínculo caso'),
        ),
    ]
