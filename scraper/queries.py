import graphene 

from scraper.models import Product 
from scraper.types import ProductType


class ProductQuery(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(self, info, **kwargs):
        # user = info.context.user
        # if not user.is_authenticated:
        #     raise Exception('Authentication credentials were not provided.')
        return Product.objects.all()