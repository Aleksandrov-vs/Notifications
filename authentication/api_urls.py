from django.urls import path
from authentication.views import SingUpApiView, LoginApiView, JWTAuthenticationAPIView

urlpatterns = [
    path('sing-up', SingUpApiView.as_view(), name='api_sing_up'),
    path('login', LoginApiView.as_view(), name='api_login'),
    path('JWTlogin', JWTAuthenticationAPIView.as_view(), name='api_JWT_login')
]