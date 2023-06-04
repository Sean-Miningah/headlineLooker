from typing import Any

import graphene
from graphene.types import ResolveInfo
from django.http.request import HttpRequest


class AppResolverInfo(ResolveInfo):
    context: HttpRequest


class BaseMutation(graphene.relay.ClientIDMutation):
    class Meta:
        abstract = True

    success = graphene.Boolean()

    Input = None

    @classmethod
    def mutate_and_get_payload(
        cls, root, info: AppResolverInfo, **data: Any
    ) -> "BaseMutation":
        ...