from django.db import models
from users.models import User
# Create your models here.


class Person(models.Model):
    assisted = models.BooleanField(null=True)
    responsible_advisor = models.ManyToManyField(User)