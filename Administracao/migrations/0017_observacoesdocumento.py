# Generated by Django 3.1.3 on 2020-12-14 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracao', '0016_auto_20201208_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservacoesDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('description', models.TextField(default='', max_length=2000, verbose_name='Observação')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Administracao.documento')),
            ],
            options={
                'verbose_name_plural': 'Observações do documento',
            },
        ),
    ]
