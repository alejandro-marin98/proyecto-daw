from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    id = None
    username = models.CharField(max_length=20, primary_key=True)
    biografia = models.CharField(max_length=1000, default='', blank=True)
    class Meta:
        db_table = 'login_user'