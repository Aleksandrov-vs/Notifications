from authentication import views
from django.urls import path
from authentication.views import ChangePasswordViews, SingUpApiView, LoginApiView

urlpatterns = [
    path('sign-up', SingUpApiView.as_view(), name='sign_up'),
    path('settings', ChangePasswordViews.as_view(), name='change_password'),
]