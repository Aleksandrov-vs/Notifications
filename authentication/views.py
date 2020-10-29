from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from authentication.forms import ChangePasswordForm, SingUpForm
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.serializers import SingUpSerializer
from users.models import User
from users.serializers import UserSerializer
import json
from authentication.serializers import LoginSerializer

# class SingUpView(APIView):
#
#     def get(self, request):
#         form = SignupForm()
#         return render(request, 'registration/sign-up.html', context={'form': form})
#
#     def post(self, request):
#         form = SignupForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/dashboard')
#         return render(request, 'registration/sign-up.html', context={'form': form})


class SingUpApiView(APIView):

    def get(self, request):
        serializer = SingUpSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = SingUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request, user)
        print(serializer.error_messages, serializer.errors)
        return Response(user.email)


class ChangePasswordViews(LoginRequiredMixin, View):
    login_url = '/account/login'

    def get(self, request):
        form = ChangePasswordForm(request.user)
        return render(request, 'registration/change_password.html', {'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            update_session_auth_hash(request, form.save())
        return render(request, 'registration/change_password.html',
                      context={'request': request, 'form': form})


class LoginApiView(APIView):

    def get(self, request):
        serializer = LoginSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        u = User.objects.get(email=serializer.validated_data.get('email'))
        login(request, u)
        return Response(u.email)