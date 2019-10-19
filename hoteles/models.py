from django.db import models

# Create your models here.

class Hotel(models.Model):
    """Modelo de hoteles"""
    city = models.CharField(max_length=100)
    User = models.CharField(max_length=100)
    foto = models.CharField(max_length=200)