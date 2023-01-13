from django.db import models

# Create your models here.

class Robot(models.Model):
    name = models.CharField(max_length=30)
    health = models.IntegerField()
