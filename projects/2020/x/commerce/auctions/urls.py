from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<str:listingTitle>", views.listing, name="listing"),
    path("new", views.new, name="new"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("category", views.category, name="category")
]