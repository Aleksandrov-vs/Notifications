from django.urls import path
from groups import views

urlpatterns = [
    path('view_groups', views.DashboardGroupsApiView.as_view(), name='api_groups'),
    path('group/<group_id>', views.ViewGroupApiView.as_view(), name='api_view_group'),
    path('delete_user/<group_id>/<telegram_user_id>', views.DeleteTelegramUserApiView.as_view()),
]