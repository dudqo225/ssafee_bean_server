from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'avatar_thumbnail', 'mbti', 'pay', 'mileage',)

class UserAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'avatar_thumbnail',)
    
class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('avatar_thumbnail', 'mbti', 'pay', 'mileage',)

class UserMileageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('mileage')
    