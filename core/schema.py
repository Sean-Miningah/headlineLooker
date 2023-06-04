from typing import cast


from graphene import Field, ObjectType, Schema
from graphene_django.debug import DjangoDebug
from user.mutations import UsersMutations
from user.queries import UsersQuery


class AppQuery(UsersQuery):
    """root query"""

    debug = Field(DjangoDebug, name="_debug")


class AppMutation(UsersMutations):
    """root mutation"""


schema = Schema(query=cast(ObjectType, AppQuery), mutation=AppMutation)