# Generated by Django 3.1.3 on 2020-12-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administracao', '0005_auto_20201204_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Último login'),
        ),
    ]