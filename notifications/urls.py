from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.urls import path

urlpatterns = [
    url('account/', include('django.contrib.auth.urls')),
    url('account/', include('authentication.urls')),
    url('dashboard/', include('groups.urls')),
    url('dashboard/', include('message.urls')),
    path('admin/', admin.site.urls),
    url('', include('core.urls')),
]
