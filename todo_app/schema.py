import graphene
import issues.query
from issues.mutations import CreateIssue

class Query(issues.query.Query, graphene.ObjectType):
    pass

class Mutations(graphene.ObjectType):
    create_issue = CreateIssue.Field()

SCHEMA = graphene.Schema(query=Query, mutation=Mutations)
