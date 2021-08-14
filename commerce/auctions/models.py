from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    id = models.AutoField(primary_key = True, default = None)
    title = models.CharField(max_length = 64, help_text = "Enter listing's title")
    description = models.TextField(help_text = "Enter item's description")
    beginningBid = models.FloatField(help_text = "Enter minimum price of item")
    img = models.URLField(max_length = 200, blank = True, help_text = "*Optional* Enter image URL")
    category = models.CharField(max_length = 64, blank = True, help_text = "*Optional* Enter listing category")
    active = models.BooleanField(default = True)
    creator = models.CharField(max_length = 64, help_text = "Enter listing's creator:", default="None")