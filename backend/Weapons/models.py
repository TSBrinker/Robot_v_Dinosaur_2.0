from django.db import models

# Create your models here.

class Weapon(models.Model):
    name = models.CharField(max_length=30)
    attack_power = models.IntegerField()
    speed = models.IntegerField()
