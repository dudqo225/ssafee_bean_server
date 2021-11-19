from django.db import models

# User Model 확장
from django.contrib.auth.models import AbstractUser
# 이미지 사용
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    avatar_thumbnail = ProcessedImageField(upload_to='avatars', 
                                           processors=[ResizeToFill(300, 300)],
                                           format='JPEG',
                                           options={'quality': 100},
                                           blank=True,
                                           )
    MBTI_CHOICES = [
        ('NULL', '없음'),
        ('ISTJ', 'ISTJ'),
        ('ISTP', 'ISTP'),
        ('ISFJ', 'ISFJ'),
        ('ISFP', 'ISFP'),
        ('INTJ', 'INTJ'),
        ('INTP', 'INTP'),
        ('INFJ', 'INFJ'),
        ('INFP', 'INFP'),
        ('ESTJ', 'ESTJ'),
        ('ESTP', 'ESTP'),
        ('ESFJ', 'ESFJ'),
        ('ESFP', 'ESFP'),
        ('ENTJ', 'ENTJ'),
        ('ENTP', 'ENTP'),
        ('ENFJ', 'ENFJ'),
        ('ENFP', 'ENFP'),
    ]
    mbti = models.CharField(max_length=10, choices=MBTI_CHOICES, default='NULL')
    pay = models.BooleanField(default=False)
    mileage = models.IntegerField(default=0)

