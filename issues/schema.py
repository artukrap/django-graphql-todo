from graphene import Node
from graphene_django import DjangoObjectType
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
        if info.context.user is None:
            return None

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
