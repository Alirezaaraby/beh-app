from django.urls import path, include
from .views import *

urlpatterns = [
    path("", overheads, name="overheads"),
    path("create", overheads_create, name="overheads-create"),
    # path("edit/<int:id>", overheads_edit, name="overheads-edit"),
    # path("delete/<int:id>", overheads_delete, name="overheads-delete"),
    # path("details/<int:id>", overheads_details, name="overheads-details")
]
