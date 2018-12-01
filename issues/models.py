from django.db import models

class Issue(models.Model):
  title = models.CharField(max_length=200, blank=False)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

class Comment(models.Model):
  issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True)
  message = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

