import factory
from todo_app.factory import UserFactory
from . import models


class IssueFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Issue

    user = factory.SubFactory(UserFactory)
    title = 'Test issue'

class CommentFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Comment

    user = factory.SubFactory(UserFactory)
    issue = factory.SubFactory(IssueFactory)
    message = "My random message"

