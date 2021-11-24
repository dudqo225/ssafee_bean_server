from rest_framework import serializers
from .models import Genre, Movie, UserMovie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class UserMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    user_movie = UserMovieSerializer(many=True)
    like_user_count = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'story', 'original_title', 'rank', 'release_date', 'poster_path', 'genres', 'like_users', 'user_movie', 'like_user_count']

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'