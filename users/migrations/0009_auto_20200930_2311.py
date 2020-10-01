# Generated by Django 3.1 on 2020-09-30 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200930_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onduty',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='duties', to=settings.AUTH_USER_MODEL),
        ),
    ]
