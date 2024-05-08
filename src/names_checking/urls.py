from django.contrib import admin
from django.urls import path, include

import api
from api import urls
from .swagger import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api.urls)),
]

urlpatterns += doc_urls
