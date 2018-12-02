import graphene
from graphene_django import DjangoObjectType
from .models import Issue, Comment

class IssueType(DjangoObjectType):
    class Meta:
        model = Issue

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class Query():
    issue = graphene.Field(IssueType, id=graphene.Int())
    issues = graphene.List(IssueType)

    comments = graphene.List(CommentType)

    def resolve_issues(self, _info):
        return Issue.objects.all()

    def resolve_issue(self, _info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Issue.objects.get(pk=id)

        return None