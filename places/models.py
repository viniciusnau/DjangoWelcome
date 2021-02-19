from django.db import models
from django.utils import timezone

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
