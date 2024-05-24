from django.urls import path, include
from .views import *

urlpatterns = [
    path("", indicators, name="indicators"),
    path("create", indicators_create, name="indicators-create"),
    path("edit/<int:id>", indicators_edit, name="indicators-edit"),
    path("delete/<int:id>", indicators_delete, name="indicators-delete"),
    path("items/create", indicator_items_create, name="indicator-items-create"),
    path("items/edit/<int:id>", indicator_items_edit, name="indicator-items-edit"),
    path("items/delete/<int:id>", indicator_items_delete, name="indicator-items-delete"),
]
