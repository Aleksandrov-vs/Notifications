from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/groups', views.dashboard_groups, name='groups'),
    path('dashboard/group/<group_id>', views.view_group, name='view_group'),
    path('dashboard/group/<group_id>/delete', views.delete_group, name='delete_group'),
]