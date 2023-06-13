from django.db import models

from core.models import BaseModel


class Product(BaseModel):
	"""
	Product model that stores data scraped, discount is in percentage and price is in Ksh
	"""
 
	brand = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	price = models.CharField(max_length=255)
	old_price = models.CharField(max_length=255)
	discount = models.CharField(max_length=255)
	official_store = models.CharField(max_length=255)