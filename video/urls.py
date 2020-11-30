from django.urls import path
from .views import VideoApiView
urlpatterns = [
    path('', VideoApiView.as_view(), name='api_video')
]