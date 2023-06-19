from core.mutations import AppResolverInfo
from graphene import ID, Boolean, ObjectType, String, relay
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload
from user.models import Following, User

####################################
#    Object Types
####################################


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password",)
        interfaces = (relay.Node,)


class UserDetailsType:
    email = String(required=True)
    username = String(required=True)


####################################
#    Input Types
####################################


class UserCreateInputType(UserDetailsType):
    password = String(required=True)
    confirm_password = String(required=True)


class UserUpdateInputType:
    email = String()
    username = String()
