from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = "cacheapp"

urlpatterns = [
    path("", cache_page(60 * 16)(views.index), name="index"),
]
