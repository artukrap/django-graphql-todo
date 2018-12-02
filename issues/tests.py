from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Issue, Comment

class IssueModelTests(TestCase):
    def test_issue_can_be_created(self):
        Issue(title="Test issue").save()

        self.assertEqual(len(Issue.objects.all()), 1)
        self.assertEqual(Issue.objects.first().title, "Test issue")

    def test_issue_creation_without_title(self):
        with self.assertRaises(ValidationError):
            Issue().full_clean()

class CommentModelTests(TestCase):
    def test_comment_creation_under_issue(self):
        issue = Issue.objects.create(title="Connected issue")
        comment = Comment.objects.create(message="Test message", issue=issue)

        self.assertEqual(len(Comment.objects.all()), 1)
        self.assertEqual(comment.message, "Test message")
        self.assertEqual(comment.issue.title, "Connected issue")
        self.assertEqual(issue.comment_set.first is None, False)
