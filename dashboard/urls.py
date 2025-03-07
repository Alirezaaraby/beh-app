from django.urls import path, include
from .views import *
# import substitute.views as sub

urlpatterns = [
    path("", index, name="dashboard"),
    
    path("daily-evaluation/", daily_evaluation , name="daily-evaluation"),
    path("daily-evaluation/complete", daily_evaluation_complete , name="daily-evaluation-complete"),
    path("daily-evaluation/all", daily_evaluation_all , name="daily-evaluation-all"),
    path("daily-evaluation/details/<int:id>", daily_evaluation_details , name="daily-evaluation-details"),
    path("daily-evaluation/create", daily_evaluation_create , name="daily-evaluation-create"),
    path("daily-evaluation/edit/<int:id>", daily_evaluation_edit , name="daily-evaluation-edit"),
    path("daily-evaluation/delete/<int:id>", daily_evaluation_delete , name="daily-evaluation-delete"),
    path("daily-evaluation/accept/<int:id>", daily_evaluation_accept , name="daily-evaluation-accept"),
    path("daily-evaluation/modify/<int:id>", daily_evaluation_modify , name="daily-evaluation-modify"),
    path("daily-evaluation/reject/<int:id>", daily_evaluation_reject , name="daily-evaluation-reject"),
    path("daily-evaluation/history/<int:id>", history , name="history"),

    path("daily-evaluation/sub/", substitute_show, name="daily-substitute-show"),
    path("daily-evaluation/substitute/create/<int:id>", substitute_create, name="daily-substitute-create"),

    path("editor", editor , name="editor"),

    path("personnel/", personnel , name="personnel"),
    path("overheads/", include("overheads.urls")),
    path("groups/", include("groups.urls")),
    path("test/", test),

    path("indicators/", include("indicators.urls")),

    path("substitute/", include("substitute.urls")),
    path("logs/", include("logs.urls")),
    path("reports/", include("reports.urls") , name="reports"),

    path('ajax/load-indicator-items/', load_indicator_items, name='ajax-load-indicator-items'),
    path('ajax/load-indicator-item-range/', load_indicator_item_range, name='ajax-load-indicator-item-range'),
    path('ajax/autocomplete/', autocomplete, name='autocomplete'),
    # path("", index, name="home")
    # path('', include('django.contrib.auth.urls'))
]
