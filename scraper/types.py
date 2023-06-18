from graphene_django import DjangoObjectType

from scraper.models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product