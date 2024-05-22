from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="dashboard"),
    
    path("daily-evaluation/", daily_evaluation , name="daily-evaluation"),
    path("daily-evaluation/create", daily_evaluation_create , name="daily-evaluation-create"),

    path("editor", editor , name="editor"),

    path("personnel/", personnel , name="personnel"),
    path("groups/", include("groups.urls")),

    path("indicators/", include("indicators.urls")),

    path("substitute/", substitute , name="substitute"),
    path("logs/", logs , name="logs"),
    path("reports/", reports , name="reports"),
    # path("", index, name="home")
    # path('', include('django.contrib.auth.urls'))
]
