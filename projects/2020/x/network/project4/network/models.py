from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    post_id = models.AutoField(primary_key = True, default=None),
    poster = models.CharField(max_length = 64, default=None),
    content = models.TextField(max_length = 300, default=None),
    time = models.TimeField(auto_now=False, auto_now_add=False, default=None),
    date = models.DateField(default=None)