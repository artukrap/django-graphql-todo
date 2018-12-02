import pytest
from django.test import TestCase
from django.core.exceptions import ValidationError
from graphene.test import Client
from dotmap import DotMap
from snapshottest import TestCase as TestCaseSnapshot
from todo_app.schema import SCHEMA
from .models import Issue, Comment
from .factory import IssueFactory, CommentFactory

@pytest.mark.django_db
class IssueModelTests(TestCase):
    def test_issue_can_be_created(self):
        Issue(title="Test issue").save()

        self.assertEqual(len(Issue.objects.all()), 1)
        self.assertEqual(Issue.objects.first().title, "Test issue")

    def test_issue_creation_without_title(self):
        with self.assertRaises(ValidationError):
            Issue().full_clean()

@pytest.mark.django_db
class CommentModelTests(TestCase):
    def test_comment_creation_under_issue(self):
        issue = Issue.objects.create(title="Connected issue")
        comment = Comment.objects.create(message="Test message", issue=issue)

        self.assertEqual(len(Comment.objects.all()), 1)
        self.assertEqual(comment.message, "Test message")
        self.assertEqual(comment.issue.title, "Connected issue")
        self.assertEqual(issue.comment_set.first is None, False)

@pytest.mark.django_db
class GraphQLTests(TestCaseSnapshot):
    def setUp(self):
        self.issue = IssueFactory()
        CommentFactory(issue=self.issue, user=self.issue.user)

        self.user = self.issue.user
        self.client = Client(SCHEMA)

    def test_all_issues(self):
        response = self.client.execute("""
            {
                issues {
                    edges {
                        node {
                            id
                            title
                            commentSet {
                                edges {
                                    node {
                                        id
                                        message
                                    }
                                }
                            }
                        }
                    }
                }
            }
        """, context=DotMap(user=self.user))

        self.assert_match_snapshot(response)

    def test_issue_query(self):
        response = self.client.execute("""
            {
                issue(id: "SXNzdWVOb2RlOjE=") {
                    id
                    title
                    commentSet {
                        edges {
                            node {
                                id
                                message
                            }
                        }
                    }
                }
            }
        """, context=DotMap(user=self.user))

        self.assert_match_snapshot(response)
