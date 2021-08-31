from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:targetPage>", views.entry, name="entry"),
    path("search/<str:targetPage>", views.entry, name="search"),
    path("new", views.new, name="new"),
    path("random", views.random, name="random"),
    path("wiki/edit/<str:pageTitle>", views.edit, name="edit")
]
