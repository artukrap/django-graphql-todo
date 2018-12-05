import graphene
import issues.query

class Query(issues.query.Query, graphene.ObjectType):
    pass

SCHEMA = graphene.Schema(query=Query)
