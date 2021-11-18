from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import Movie
from .serializers import MovieSerializer, MovieListSerializer


# READ & CREATE
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    # 전체 영화 조회
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    # 영화 데이터 생성
    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


# READ & UPDATE & DELETE - 영화 상세 정보
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    # 영화 상세 정보 조회
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    # 영화 상세 정보 수정
    # elif request.method == 'PUT':
    #     serializer = MovieSerializer(movie, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

    # 영화 상세 정보 삭제
    # elif request.method == 'DELETE':
    #     movie.delete()
    #     data = {
    #         'delete': f'영화 데이터 {movie_pk}번이 삭제되었습니다.'
    #     }
    #     return Response(data, status=status.HTTP_204_NO_CONTENT)