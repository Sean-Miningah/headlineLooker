from typing import cast
from graphene import Field, ObjectType, Schema
from graphene_django.debug import DjangoDebug
import graphql_jwt

from user.mutations import UsersMutations
from user.queries import UsersQuery
from scraper.queries import ProductQuery


class AppQuery(UsersQuery, ProductQuery, ObjectType):
    """root query"""

    debug = Field(DjangoDebug, name="_debug")


class AppMutation(UsersMutations, ObjectType):
    """root mutation"""
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = Schema(query=AppQuery, mutation=AppMutation)