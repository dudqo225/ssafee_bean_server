# Generated by Django 3.2.9 on 2021-11-17 02:42

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to='avatars'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mbti',
            field=models.CharField(choices=[('ISTJ', 'ISTJ'), ('ISTP', 'ISTP'), ('ISFJ', 'ISFJ'), ('ISFP', 'ISFP'), ('INTJ', 'INTJ'), ('INTP', 'INTP'), ('INFJ', 'INFJ'), ('INFP', 'INFP'), ('ESTJ', 'ESTJ'), ('ESTP', 'ESTP'), ('ESFJ', 'ESFJ'), ('ESFP', 'ESFP'), ('ENTJ', 'ENTJ'), ('ENTP', 'ENTP'), ('ENFJ', 'ENFJ'), ('ENFP', 'ENFP')], default='없음', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='mileage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='pay',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]