from django.db import models

# Create your models here.

class Product(models.Model):
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    old_price = models.CharField(max_length=255)
    discount = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    

