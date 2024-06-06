from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("permissions/<int:id>", views.permissions, name="permissions"),
    path("edit/<int:id>", views.edit, name="edit-user"),
    path("delete/<int:id>", views.delete, name="delete-user"),
]
