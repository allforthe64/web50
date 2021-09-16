from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    post_id = models.AutoField(primary_key=True, default=None),
    poster = models.ForeignKey(User, on_delte=models.CASCADE, related_name="user"),
    date = models.DateField(default=None),
    time = models.TimeField(auto_now_add=True, default=None),
    content = models.TextField(default=None)


