from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class listing(models.Model):
    title = models.CharField(max_length = 64, primary_key = True, help_text = "Enter listing's title")
    descrpt = models.TextField(help_text = "Enter item's description")
    beginningBid = models.IntegerField(help_text = "Enter minimum price of item")
    img = models.URLField(max_length = 200, blank = True, help_text = "*Optional* Enter image URL")
    category = models.CharField(max_length = 64, blank = True, help_text = "*Optional* Enter listing category")