from django.db import models

# User Model 확장
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

