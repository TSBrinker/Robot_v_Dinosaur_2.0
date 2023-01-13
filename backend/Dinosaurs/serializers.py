from rest_framework import serializers
from .models import Dinosaur

class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ['id', 'name', 'health', 'attack_power', 'speed', 'armor']