from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="dashboard"),
    
    path("daily-evaluation/", daily_evaluation , name="daily-evaluation"),
    path("daily-evaluation/create", daily_evaluation_create , name="daily-evaluation-create"),

    path("editor", editor , name="editor"),

    path("personnel/", personnel , name="personnel"),
    path("groups/", include("groups.urls")),
    path("test/", test),

    path("indicators/", include("indicators.urls")),

    path("substitute/", substitute , name="substitute"),
    path("logs/", logs , name="logs"),
    path("reports/", reports , name="reports"),

    path('ajax/load-indicator-items/', load_indicator_items, name='ajax-load-indicator-items'),
    path('ajax/load-indicator-item-range/', load_indicator_item_range, name='ajax-load-indicator-item-range'),
    path('ajax/autocomplete/', autocomplete, name='autocomplete'),
    # path("", index, name="home")
    # path('', include('django.contrib.auth.urls'))
]
