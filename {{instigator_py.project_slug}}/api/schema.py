import graphene
from {{instigator_py.project_slug}}.users.api.queries import AuthQuery
from {{instigator_py.project_slug}}.users.api.mutations import AuthMutation


class Query(
        AuthQuery,
        graphene.ObjectType):
    pass


class Mutation(
        AuthMutation,
        graphene.ObjectType):
    pass
