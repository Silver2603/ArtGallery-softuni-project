# Generated by Django 5.0.3 on 2024-04-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artpiece',
            name='art_piece',
            field=models.URLField(unique=True),
        ),
    ]