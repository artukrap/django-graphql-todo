from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Issue, Comment

class IssueNode(DjangoObjectType):
    class Meta:
        model = Issue
        filter_fields = {
            'title': ['exact', 'icontains']
        }
        interfaces = (relay.Node, )

class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        filter_fields = {
            'message': ['icontains']
        }
        interfaces = (relay.Node, )


class Query():
    issue = relay.Node.Field(IssueNode)
    issues = DjangoFilterConnectionField(IssueNode)

    comments = DjangoFilterConnectionField(CommentNode)

    def resolve_issues(self, _info, **kwargs):
        return Issue.objects.all()

    def resolve_issue(self, _info, **kwargs):
        issue_id = kwargs.get("id")

        if issue_id is not None:
            return Issue.objects.get(pk=issue_id)

        return None
