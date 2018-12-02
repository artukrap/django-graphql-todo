"""Main app GraphQL schema"""
import graphene
import issues.schema

class Query(issues.schema.Query, graphene.ObjectType):
    pass

SCHEMA = graphene.Schema(query=Query)
