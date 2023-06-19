import uuid
from typing import Any

import graphene
import graphql_jwt
from core.mutations import BaseMutation
from graphql import GraphQLError
from graphql_jwt.decorators import login_required
from user.models import User
from user.types import ( UserCreateInputType, UserNode,
                         UserUpdateInputType)

####################################
#    Users Mutations
####################################


class CreateUserMutation(BaseMutation):
    Input = UserCreateInputType

    user = graphene.Field(UserNode, required=True)

    def mutate_and_get_payload(self, info, **data):
        password = data.get("password")
        confirm_password = data.pop("confirm_password")
        if not password == confirm_password:
            raise GraphQLError("password and confirm_password must match")
        print(f'------------{data}--------')
        user = User.objects.create_user(**data)

        return CreateUserMutation(success=True, user=user)


class UpdateUserMutation(BaseMutation):
    Input = UserUpdateInputType

    user = graphene.Field(UserNode)

    def mutate_and_get_payload(self, info, **data):
        current_user = info.context.user
        for key, value in data.items():
            setattr(current_user, key, value)
            current_user.save()
        return UpdateUserMutation(user=current_user, success=True)


####################################
#    Users Authentication
####################################


class UserLoginMutation(graphql_jwt.relay.JSONWebTokenMutation):
    user = graphene.Field(UserNode)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class UsersMutations(graphene.ObjectType):
    create_user = CreateUserMutation.Field(description="create a new user")
    update_user = UpdateUserMutation.Field(
        description="update the current logged in user"
    )

    login_user = UserLoginMutation.Field()
    verify_token = graphql_jwt.relay.Verify.Field()
    refresh_token = graphql_jwt.relay.Refresh.Field()