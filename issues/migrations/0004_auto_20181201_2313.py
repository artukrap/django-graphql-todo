# Generated by Django 2.1.3 on 2018-12-01 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_comment_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
