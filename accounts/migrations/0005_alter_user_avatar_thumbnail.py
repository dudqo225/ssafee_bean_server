# Generated by Django 3.2.9 on 2021-11-19 06:14

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211118_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='avatars'),
        ),
    ]