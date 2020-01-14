from django.db import models

# Create your models here.
class RentalManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if(int(postData['price']) < 100):
            errors['price'] = "Price must be more than $100."
        if(len(postData['image']) < 10):
            errors['image'] = "Image must be a link."
        if(len(postData['duration']) < 2):
            errors['duration'] = "You must state a duration!"
        if(len(postData['brand']) < 5):
            errors['brand'] = "You must state a valid brand."
        if(len(postData['model']) < 5): 
            errors['model'] = "You must state a valid model."
        return errors 
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
    objects = RentalManager()