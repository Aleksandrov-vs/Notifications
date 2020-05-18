from django.urls import path
from . import views

urlpatterns = [
    path('groups', views.dashboard_groups, name='groups'),
    path('group/<group_id>', views.view_group, name='view_group'),
    path('group/<group_id>/delete', views.delete_group, name='delete_group'),
]