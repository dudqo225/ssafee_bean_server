# Generated by Django 3.2.9 on 2021-11-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20211124_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(default=0),
        ),
    ]