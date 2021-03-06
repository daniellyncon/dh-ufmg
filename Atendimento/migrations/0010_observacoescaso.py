# Generated by Django 3.1.3 on 2020-12-14 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0009_auto_20201207_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservacoesCaso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('description', models.TextField(default='', max_length=2000, verbose_name='Observação')),
                ('caso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Atendimento.caso')),
            ],
            options={
                'verbose_name_plural': 'Observações do caso',
            },
        ),
    ]
