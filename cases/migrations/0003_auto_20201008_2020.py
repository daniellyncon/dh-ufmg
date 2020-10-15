# Generated by Django 3.1 on 2020-10-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_auto_20201006_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='related_areas',
            field=models.CharField(blank=True, choices=[('1', 'Administrativo'), ('2', 'Ambiental'), ('3', 'Cível'), ('4', 'Consumidor'), ('5', 'Criminal'), ('6', 'Família'), ('7', 'Ambiental'), ('8', 'Previdenciário'), ('9', 'Sucessões'), ('10', 'Societário'), ('11', 'Trabalhista'), ('12', 'Tributário'), ('13', 'Contratos'), ('14', 'Internacional')], max_length=3, null=True, verbose_name='Áreas Relacionadas'),
        ),
    ]