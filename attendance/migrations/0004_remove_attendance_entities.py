# Generated by Django 3.1 on 2020-10-31 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20201031_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='entities',
        ),
    ]
