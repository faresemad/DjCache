# DjCache
Django Cache with Memchaced
# Installation

- Install Memcached on your system from :[Memcached](https://memcached.org/)
- This is also the site explaining the cache, you can refer to it :[Django Cache](https://www.tutorialspoint.com/django/django_caching.htm)

```bash
pip install pymemcache
```
# Usage
> Add this to your `settings.py`
```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
    }
}
```

## Cache whole site
> Add this code also to your `settings.py`
```python
MIDDLEWARE = [
    # ....
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    # ....
]
```

> Add Cache settings to your `settings.py`
```python
CACHE_MIDDLEWARE_ALIAS = "default"

CACHE_MIDDLEWARE_SECONDS = 60 * 15 # 15 minutes

CACHE_MIDDLEWARE_KEY_PREFIX = ""
```

## Per-View Cache
```python
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 15)  # 15 minutes
def index(request):
    return render(request, "cacheapp/index.html", {})
```

## Template Cache
```python
{% load cache %}
{% cache 500 sidebar request.user.username %}
    .. sidebar for logged in users ..
{% endcache %}
```

## Url Cache
```python
from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = "cacheapp"

urlpatterns = [
    path("", cache_page(60 * 16)(views.index), name="index"),
]
```
