from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/rank/', views.movie_rank),
    path('<int:movie_pk>/rank/<int:rank_pk>/', views.movie_rank_update_delete),
    path('<int:movie_pk>/likes/', views.movie_likes),
]