# Generated by Django 2.1.3 on 2018-12-01 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_issue_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='issues.Issue'),
        ),
    ]