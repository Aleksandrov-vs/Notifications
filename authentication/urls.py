from django.urls import path
from authentication import views

urlpatterns = [
    path('account/sign-up', views.sign_up, name='sign_up'),
    path('change_password', views.change_password, name='change_password'),
]