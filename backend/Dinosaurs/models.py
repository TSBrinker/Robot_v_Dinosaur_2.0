from django.db import models

# Create your models here.

class Dinosaur(models.Model):
    name = models.CharField(max_length=30)
    health = models.IntegerField()
    attack_power = models.IntegerField()
    speed = models.IntegerField()
    armor = models.IntegerField()
