from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', views.users),
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('<str:username>/', views.user_detail),
    path('<str:username>/mileage/', views.user_mileage),
]