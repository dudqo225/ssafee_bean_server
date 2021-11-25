from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import Genre, Movie, UserMovie
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer, UserMovieSerializer
from django.db.models import Q

# READ & CREATE
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    # 전체 영화 조회
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        # 영화 타이틀 검색 기능
        q = request.GET.get('q', '')
        if q:
            movies = get_list_or_404(Movie, Q(title__icontains=q) | Q(original_title__icontains=q))
        # paginator = Paginator(movies, 10)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    # 영화 데이터 생성
    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

# 장르 리스트 GET
@api_view(['GET'])
@permission_classes([AllowAny])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

# 장르 영화 리스트 GET
@api_view(['GET'])
@permission_classes([AllowAny])
def genre_movie_list(request, genre_pk):
    movies = Movie.objects.filter(genres__in=[genre_pk]).order_by('-rank', 'title')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    

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

    if request.method == 'GET':
        user_movie = get_object_or_404(UserMovie, movie=movie_pk, user=request.user.pk)
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
def movie_recommendation(request, mode, mode_pk):
    # mode - genre, rank, mbti
    # if mode == 'genre':
    #     movies = Movie.objects.filter(genres__in=[mode_pk]).order_by('-rank', 'title')[:10]
    #     serializer = MovieListSerializer(movies, many=True)
    #     return Response(serializer.data)
    if mode == 'rank':
        user_movie = get_list_or_404(UserMovie, user=mode_pk)
        serializer = UserMovieSerializer(user_movie, many=True)
        return Response(serializer.data)
    elif mode == 'mbti':
        # ISTJ
        if mode_pk == 1:
            movies = get_list_or_404(Movie, genres__in=[53, 9648])
        # ISTP
        elif mode_pk == 2:
            movies = get_list_or_404(Movie, genres__in=[14, 878])
        # ISFJ
        elif mode_pk == 3:
            movies = get_list_or_404(Movie, genres__in=[18, 53])
        # ISFP
        elif mode_pk == 4:
            movies = get_list_or_404(Movie, genres__in=[10770, 18, 10751])
        # INTJ
        elif mode_pk == 5:
            movies = get_list_or_404(Movie, genres__in=[9648, 18, 10749, 10402])
        # INTP
        elif mode_pk == 6:
            movies = get_list_or_404(Movie, genres__in=[10749, 18])
        # INFJ
        elif mode_pk == 7:
            movies = get_list_or_404(Movie, genres__in=[53, 18, 10751])
        # INFP
        elif mode_pk == 8:
            movies = get_list_or_404(Movie, genres__in=[18, 10749, 878, 16])
        # ESTJ
        elif mode_pk == 9:
            movies = get_list_or_404(Movie, genres__in=[28, 10749])
        # ESTP
        elif mode_pk == 10:
            movies = get_list_or_404(Movie, genres__in=[80, 53])
        # ESFJ
        elif mode_pk == 11:
            movies = get_list_or_404(Movie, genres__in=[10749, 35, 10752])
        # ESFP
        elif mode_pk == 12:
            movies = get_list_or_404(Movie, genres__in=[10749, 18, 35])
        # ENTJ
        elif mode_pk == 13:
            movies = get_list_or_404(Movie, genres__in=[10402, 80, 53])
        # ENTP
        elif mode_pk == 14:
            movies = get_list_or_404(Movie, genres__in=[99, 18])
        # ENFJ
        elif mode_pk == 15:
            movies = get_list_or_404(Movie, genres__in=[10749, 14, 12])
        # ENFP
        elif mode_pk == 16:
            movies = get_list_or_404(Movie, genres__in=[9648, 18, 53, 27, 36, 10752])
        
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)    