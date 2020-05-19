from django.urls import path
from message import views

urlpatterns = [
    path('', views.DashboardMessagesView.as_view(), name='dashboard'),
    # path('notification/<id>', views.view, name='dashboard')
]