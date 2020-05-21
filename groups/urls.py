from django.urls import path
from groups import views

urlpatterns = [
    path('groups', views.DashboardGroupsView.as_view(), name='groups'),
    path('group/<group_id>', views.ViewGroupView.as_view(), name='view_group'),
    path('group/<group_id>/delete', views.DeleteGroupView.as_view(), name='delete_group'),
    path('group/<group_id>/<telegram_user_id>/delete_user/', views.DeleteUser.as_view(), name= 'delete_telegram_user'),
]