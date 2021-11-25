from django.db import models
from django.conf import settings

# Review
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    # 좋아요한 유저
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)
    # movie와 1:N 연결
    # movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title

# Comment
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 리뷰
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    # 작성 유저
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.content