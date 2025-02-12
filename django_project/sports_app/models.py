# Create your models here.
from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    season = models.CharField(max_length=100)
    indoor = models.BooleanField(default=False)
    outdoor = models.BooleanField(default=True)

    def __str__(self):
        return self.name
