from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from .schema import IssueNode, CommentNode
from .models import Issue

class Query():
    issue = Node.Field(IssueNode)
    issues = DjangoFilterConnectionField(IssueNode)

    comments = DjangoFilterConnectionField(CommentNode)

    def resolve_issues(self, info):
        if info.context.user is None:
            return Issue.objects.none()
        else:
            return Issue.objects.filter(user=info.context.user)
