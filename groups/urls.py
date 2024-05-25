from django.urls import path, include
from .views import *

urlpatterns = [
    path("", groups, name="groups"),
    path("create", groups_create, name="groups-create"),
    path("edit/<int:id>", groups_edit, name="groups-edit"),
    path("delete/<int:id>", groups_delete, name="groups-delete"),
    path("details/<int:id>", groups_details, name="groups-details"),
    path("members/create", group_members_create, name="group-members-create"),
    path("members/edit/<int:id>", group_members_edit, name="group-members-edit"),
    path("members/delete/<int:id>", group_members_delete, name="group-members-delete"),
]
