# Generated by Django 5.0.6 on 2024-05-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_blogpost_is_published_alter_blogpost_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]