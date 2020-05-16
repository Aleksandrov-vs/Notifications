from django.urls import path
from core import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.index, name='index'),
]