# Generated by Django 3.2.9 on 2021-11-18 04:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_alter_review_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
