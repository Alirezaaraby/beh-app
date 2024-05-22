from django.urls import path, include
from .views import *

urlpatterns = [
    path("", indicators, name="indicators"),
    path("create", indicators_create, name="indicators-create"),
    path("items/create", indicator_items_create, name="indicator-items-create"),
]
