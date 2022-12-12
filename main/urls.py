from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("posts/", views.posts, name="posts"),
    path("newpost/", views.newpost, name="newpost")
]
