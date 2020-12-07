# Generated by Django 3.1.3 on 2020-12-07 23:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0006_auto_20201207_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='first_appointment_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 7, 23, 0, 7, 898058, tzinfo=utc), verbose_name='Data do primeiro atendimento'),
        ),
    ]
