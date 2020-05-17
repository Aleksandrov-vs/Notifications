from django.urls import path
import groups.views
import core.views

urlpatterns = [
    path('', core.views.index, name='index'),
    path('dashboard', core.views.dashboard, name='dashboard'),
]