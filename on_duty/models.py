from users.models import User
from django.db import models

# Create your models here.


class OnDuty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="duties", default=None)
    day_of_the_week = models.IntegerField(verbose_name="Dia da semana")
    start_time = models.TimeField(verbose_name="Início plantão")
    end_time = models.TimeField(verbose_name="Fim plantão")