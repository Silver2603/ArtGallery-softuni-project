# Generated by Django 5.0.3 on 2024-04-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0008_comments_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
