from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Issue, Comment

class CommentInline(admin.TabularInline):
  model = Comment
  max_num = 1

@admin.register(Issue)
class IssueAdmin(VersionAdmin):
  inlines = [
    CommentInline,
  ]
