# Generated by Django 3.1 on 2020-10-08 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20201006_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='related_law_suit',
        ),
    ]