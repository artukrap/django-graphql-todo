# Generated by Django 2.1.3 on 2018-12-01 22:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
