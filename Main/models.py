from django.db import models

# Create your models here.
class Guitar(models.Model):
    sale = models.IntegerField()
    image = models.CharField(max_length=255)
    price = models.FloatField()
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Rental(models.Model):
    price = models.FloatField()
    image = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)