from users.models import User
from django.db import models

# Create your models here.


class OnDuty(models.Model):
    DAYS = (('1', 'Segunda-feira'), ('2', 'Terça-feira'), ('3', 'Quarta-feira'), ('4', 'Quinta-feira'),
                ('5', 'Sexta-feira'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="duties", default=None)
    day_of_the_week = models.CharField(max_length=10, choices=DAYS, blank=True, null=True, verbose_name='Dia da semana')
    start_time = models.TimeField(verbose_name="Início plantão")
    end_time = models.TimeField(verbose_name="Fim plantão")