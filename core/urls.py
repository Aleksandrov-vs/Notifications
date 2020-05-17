from django.urls import path
import groups.views
import core.views

urlpatterns = [
    path('', core.views.index, name='index'),
    path('dashboard', core.views.dashboard, name='dashboard'),
    path('account/sign-up', core.views.sign_up, name='sign_up'),
    path('dashboard/groups', groups.views.dashboard_groups, name='dashboard'),
    path('dashboard/group/<group_id>', groups.views.view_group, name='view_group'),
    path('dashboard/group/<group_id>/delete', groups.views.delete_group, name='delete_group'),
]