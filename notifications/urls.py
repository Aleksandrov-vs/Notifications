from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.urls import path

import core.urls as urls_core

urlpatterns = [
    url('account/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    url('', include('groups.urls')),
] + urls_core.urlpatterns
