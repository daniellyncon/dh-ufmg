# Generated by Django 3.1 on 2020-10-30 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_auto_20201024_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='registration_date',
            field=models.DateField(auto_now=True, verbose_name='Data de cadastro'),
        ),
    ]
