# Generated by Django 3.1 on 2020-10-31 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20201031_0303'),
        ('people', '0008_auto_20201031_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.ManyToManyField(blank=True, related_name='person_document', to='documents.Document'),
        ),
    ]
