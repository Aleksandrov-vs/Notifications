from django.urls import path
from message import views

urlpatterns = [
    path('', views.dashboard, name='dashboard')
]