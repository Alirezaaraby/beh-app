from django.urls import path, include
from .views import *
import substitute.views as sub

urlpatterns = [
    path("", substitute, name="substitute"),
    path('get-user-permissions/', get_user_permissions, name='get_user_permissions'),
]