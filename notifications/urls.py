from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.urls import path

urlpatterns = [
    url('account/', include('django.contrib.auth.urls')),
    url('account/', include('authentication.urls')),
    url('dashboard/', include('groups.urls')),
    url('dashboard/', include('message.urls')),
    url('api/v1/account/', include('authentication.api_urls')),
    url('api/v1/', include('groups.api_urls')),
    path('admin/', admin.site.urls),
    url('api/v1/video', include('video.urls')),
    url('', include('core.urls')),
]
