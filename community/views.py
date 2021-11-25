from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status

from .models import Review, Comment
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer


# READ & CREATE - 리뷰
@api_view(['GET', 'POST'])
def review_list(request):
    # 전체 리뷰 조회
    if request.method == 'GET':
        reviews = Review.objects.all().order_by('-pk')
        reviews = get_list_or_404(reviews)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    # 리뷰 생성
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# READ & UPDATE & DELETE - 리뷰 상세 정보
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    # 리뷰 상세 정보 조회
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 리뷰 작성자만 수정 및 삭제 가능
    if not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    # 리뷰 상세 정보 수정
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 리뷰 상세 정보 삭제
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'리뷰 데이터 {review_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

# 리뷰 좋아요
@api_view(['GET','POST'])
def review_likes(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        if review.like_users.filter(pk=request.user.pk).exists():
            liked = True
        else:
            liked = False
        context = {
            'liked': liked,
            'likeCount': review.like_users.count()
        }
        return JsonResponse(context)
    
    else:
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            liked = False
        else:
            review.like_users.add(request.user)
            liked = True
        context = {
            'liked': liked,
            'likeCount': review.like_users.count(),
        }
        return JsonResponse(context)


# READ - 댓글 리스트
@api_view(['GET', 'POST'])
def comment_list(request, review_pk):
    # 전체 댓글 조회
    if request.method == 'GET':
        comments = Comment.objects.filter(review_id=review_pk).order_by('-pk')
        comments = get_list_or_404(comments)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    # 댓글 생성
    else:
        review = get_object_or_404(Review, pk=review_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# READ & DELETE - 세부 댓글
@api_view(['GET', 'DELETE'])
def comment_detail(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    # 개별 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    # 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
