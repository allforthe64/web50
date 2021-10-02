
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("profile/<str:username>", views.profile, name="profile"),

    #api urls
    path("like/<str:post_id>", views.like, name="like"),
    path("follow/<str:action>/<str:account>", views.follow, name="follow")
]
