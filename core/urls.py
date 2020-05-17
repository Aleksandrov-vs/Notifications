from django.urls import path
import groups.views
import core.views

urlpatterns = [
    path('', core.views.index, name='index'),
    path('dashboard', core.views.dashboard, name='dashboard'),
    path('account/sign-up', core.views.sign_up, name='sign_up'),
    path('change_password', core.views.change_password, name='change_password')
]