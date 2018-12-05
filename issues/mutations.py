import graphene
from .schema import IssueNode
from .models import Issue

class IssueInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String(required=True)

class CreateIssue(graphene.Mutation):
    class Arguments:
        issue_data = IssueInput(required=True)

    issue = graphene.Field(IssueNode)

    @staticmethod
    def mutate(_self, info, issue_data=None):
        if info.context.user is None:
            return

        issue = Issue.objects.create(
            title=issue_data.title,
            description=issue_data.description,
            user=info.context.user
        )

        return CreateIssue(issue=issue)
