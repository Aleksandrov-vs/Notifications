from authentication import views
from django.urls import path
from authentication.views import ChangePasswordViews

urlpatterns = [
    path('sign-up', views.sign_up, name='sign_up'),
    path('settings', ChangePasswordViews.as_view(), name='change_password'),
]