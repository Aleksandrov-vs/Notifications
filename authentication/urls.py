from authentication import views
from django.urls import path

urlpatterns = [
    path('sign-up', views.sign_up, name='sign_up'),
    path('settings', views.change_password, name='change_password'),
]