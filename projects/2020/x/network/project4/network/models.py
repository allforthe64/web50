from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Entry(models.Model):
    post_id = models.AutoField(primary_key=True, default=None)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    content = models.TextField(default=None)
    timestamp = model.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def serialize(self):
        return {
            "id": self.post_id,
            "poster": self.poster,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }