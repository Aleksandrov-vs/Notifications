import jwt
from django.contrib.auth import update_session_auth_hash, user_logged_in
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework_jwt.serializers import jwt_payload_handler

from authentication.forms import ChangePasswordForm, SingUpForm
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.serializers import SingUpSerializer
from notifications import settings
from users.models import User
from users.serializers import UserSerializer
import json
from authentication.serializers import LoginSerializer
from rest_framework.permissions import AllowAny

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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = LoginSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        u = User.objects.get(email=serializer.validated_data.get('email'))
        login(request, u)
        return Response(u.email)


class JWTAuthenticationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        try:
            email = request.data['email']
            password = request.data['password']

            user = User.objects.get(email=email)
            valid = user.check_password(password)
            if valid:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, settings.SECRET_KEY)
                    user_details = {}
                    user_details['name'] = "%s" % (
                        user.email)
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)
                    return Response(user_details, status=status.HTTP_200_OK)

                except Exception as e:
                     raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)
