from django.db import models


# Create your models here.


class Axis(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
