from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Entry(models.Model):
    post_id = models.AutoField(primary_key=True, default=None)
    poster = models.ForeignKey(User, on_delete=models.PROTECT, related_name="poster")
    content = models.TextField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def serialize(self):
        return {
            "id": self.post_id,
            "poster": self.poster.username,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.likes
        }

class Follow(models.Model):
    follow_id = models.AutoField(primary_key=True, default=None)
    following = models.CharField(max_length = 64, default=None)
    followedBy = models.CharField(max_length = 64, default=None)

    def serialize(self):
        return {
            "id": self.follow_id,
            "following": self.following,
            "followedBy": self.followedBy
        }