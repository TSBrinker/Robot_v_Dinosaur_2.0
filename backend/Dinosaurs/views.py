from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dinosaur
from .serializers import DinosaurSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

