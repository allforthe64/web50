
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("edit/<str:user>/<str:post_id>", views.edit, name="edit"),
    path("following", views.following, name="following"),

    #api urls
    path("like/<str:post_id>", views.like, name="like"),
    path("follow/<str:action>/<str:account>", views.follow, name="follow"),
    path("number/<str:target>", views.number, name="number"),
    path("search/<str:following>/<str:followedBy>", views.search, name="search")
]
