# Generated by Django 3.2.9 on 2021-11-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20211120_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user_name',
            field=models.CharField(default='admin', max_length=100),
            preserve_default=False,
        ),
    ]
