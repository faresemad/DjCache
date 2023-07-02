# DjCache
Django Cache with Memchaced
# Installation

- Install Memcached on your system, if you are using Linux you can download it from:[Memcached](https://memcached.org/) or you can install it using this command:
```bash
sudo apt-get update
sudo apt-get -y install memcached
```
- If you are using Windows you can download it from:[Memcached 64bit](https://static.runoob.com/download/memcached-win64-1.4.4-14.zip) or [Memcached 32bit](https://static.runoob.com/download/memcached-1.2.6-win32-bin.zip)
- You can go to this site to learn how to install it on Windows:[Memcached Windows](https://linuxhint.com/install-memcached-windows/)
- This is also the site explaining the cache, you can refer to it :[Django Cache](https://www.tutorialspoint.com/django/django_caching.htm)

- Install pymemcache using this command:
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
