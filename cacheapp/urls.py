from django.urls import path
from . import views

app_name = "cacheapp"

urlpatterns = [
    path("", views.index, name="index"),
]
