from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 15)  # 15 minutes
def index(request):
    return render(request, "cacheapp/index.html", {})
