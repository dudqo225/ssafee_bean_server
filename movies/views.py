from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import Movie, UserMovie
from .serializers import MovieSerializer, MovieListSerializer, UserMovieSerializer


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


# 영화 좋아요
@api_view(['GET','POST'])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        if movie.like_users.filter(pk=request.user.pk).exists():
            liked = True
        else:
            liked = False
        context = {
            'liked' : liked,
            'likeCount' : movie.like_users.count(),
        }
        return JsonResponse(context)

    else:
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            liked = False
        else:
            movie.like_users.add(request.user)
            liked = True
        context = {
            'liked': liked,
            'likeCount': movie.like_users.count(),
        }
        return JsonResponse(context)


# 영화 평점 생성
@api_view(['GET', 'POST'])
def movie_rank(request, movie_pk):
    user_movie = get_object_or_404(UserMovie, movie=movie_pk, user=request.user.pk)

    if request.method == 'GET':
        serializer = UserMovieSerializer(user_movie)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = UserMovieSerializer(data=request.data)
        user_id = request.data.get('user')
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie_id=movie_pk, user_id=user_id)
            return Response(serializer.data)

# 영화 평점 수정/삭제
@api_view(['PUT', 'DELETE'])
def movie_rank_update_delete(request, movie_pk, rank_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user_movie = get_object_or_404(UserMovie, pk=rank_pk)
    if request.method == 'PUT':
        serializer = UserMovieSerializer(data=request.data, instance=user_movie)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '평점이 수정되었습니다.'})
    else:
        user_movie.delete()
        return Response({'message': '평점이 삭제되었습니다.'})


# 영화 추천
@api_view(['GET'])
def movie_recommendation(request):
    pass
