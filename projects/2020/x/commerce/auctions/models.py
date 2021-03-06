from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField


class User(AbstractUser):
    pass


class Listing(models.Model):
    id = models.AutoField(primary_key = True, default = None)
    title = models.CharField(max_length = 64, help_text = "Enter listing's title")
    description = models.TextField(help_text = "Enter item's description")
    beginningBid = models.FloatField(help_text = "Enter minimum price of item")
    highestBid = models.FloatField(default = 0)
    img = models.URLField(max_length = 200, blank = True, help_text = "*Optional* Enter image URL")
    category = models.CharField(max_length = 64, blank = True, help_text = "*Optional* Enter listing category")
    active = models.BooleanField(default = True)
    creator = models.CharField(max_length = 64, help_text = "Enter listing's creator:", default="None")

class Bid(models.Model):
    id = models.AutoField(primary_key=True, default = None)
    ammount = models.FloatField(help_text = "Enter ammount to bid")
    bidder = models.CharField(max_length=64, help_text="Enter username of bidder", default="None")
    location = models.CharField(max_length=64, help_text="Enter the name of listing to bid on", default="None")

class Watchlist(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    page = models.CharField(max_length=64, help_text="Add page title")
    watcher = models.CharField(max_length=64, help_text = "Add name of watcher")

class Comment(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    page = models.CharField(max_length=64, help_text="Add page title")
    content = models.TextField(help_text = "Enter content of comment")
    commentor = models.CharField(max_length=64, help_text = "Add name of watcher")