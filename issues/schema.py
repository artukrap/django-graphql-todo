from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Issue, Comment

class IssueNode(DjangoObjectType):
    class Meta:
        model = Issue
        filter_fields = {
            'title': ['exact', 'icontains']
        }
        interfaces = (Node, )

    @classmethod
    def get_node(cls, info, issue_id):
        try:
            issue = cls._meta.model.objects.get(id=issue_id)
        except cls._meta.model.DoesNotExist:
            return None

        if info.context.user == issue.user:
            return issue
        return None

class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        filter_fields = {
            'message': ['icontains']
        }
        interfaces = (Node, )


class Query():
    issue = Node.Field(IssueNode)
    issues = DjangoFilterConnectionField(IssueNode)

    comments = DjangoFilterConnectionField(CommentNode)

    def resolve_issues(self, info, **kwargs):
        if info.context.user is None:
            return Issue.objects.none()
        else:
            return Issue.objects.filter(user=info.context.user)
