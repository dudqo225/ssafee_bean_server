from rest_framework import serializers
from .models import Review, Comment

# 댓글 Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)

# 리뷰 리스트 Serializer
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# 단일 리뷰 Serializer
class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True) # 특정 리뷰에 작성된 댓글 목록 출력
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True) # 댓글 개수 구하기

    class Meta:
        model = Review
        fields = '__all__'



