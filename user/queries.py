import graphene
from graphql import GraphQLError
from user.models import User
from user.types import UserNode


class UsersQuery(graphene.ObjectType):
    current_user = graphene.Field(UserNode)

    def resolve_current_user(self, info, **kwargs):
        if not info.context.user or not info.context.user.is_authenticated:
            raise GraphQLError("No User Logged in")
        user = User.objects.filter(id=info.context.user.id)
        return user.first()
