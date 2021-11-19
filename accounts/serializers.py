from rest_framework import serializers
from django.contrib.auth import get_user_model
# from ..movies.models import UserMovie, Movie

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'avatar_thumbnail', 'mbti', 'pay', 'mileage',)