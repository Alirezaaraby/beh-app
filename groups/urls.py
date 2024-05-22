from django.urls import path, include
from .views import *

urlpatterns = [
    path("", groups, name="groups"),
    path("create", groups_create, name="groups-create"),
    path("items/create", group_items_create, name="group-items-create"),
]
