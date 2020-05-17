from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/account/login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


