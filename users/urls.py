from django.urls import path, include
# from .views import index

urlpatterns = [
    # path("/", index, name="dashboard:home"),
    # path("dailt-evaluation/", daily_evaluation , name="dashboard:daily-evaluation")
    # path("", index, name="home")
    path('', include('django.contrib.auth.urls'))
]
