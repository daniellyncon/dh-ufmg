# Generated by Django 3.1.3 on 2020-12-05 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administracao', '0003_auto_20201204_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='address',
        ),
    ]
