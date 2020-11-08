# Generated by Django 3.1 on 2020-10-30 01:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0002_auto_20201010_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='prepared_by',
            field=models.ManyToManyField(blank=True, related_name='developer', to=settings.AUTH_USER_MODEL, verbose_name='Elaborado por'),
        ),
    ]
