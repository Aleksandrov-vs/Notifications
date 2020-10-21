from authentication import views
from django.urls import path
from authentication.views import ChangePasswordViews, SingUpView, LoginView

urlpatterns = [
    path('sign-up', SingUpView.as_view(), name='sign_up'),
    path('settings', ChangePasswordViews.as_view(), name='change_password'),
    path('api/v1/sing-up', SingUpView.as_view(), name='api_sing_up'),
    path('api/v1/login', LoginView.as_view(), name='api_login'),
]