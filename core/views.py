from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from core.forms import SignupForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/account/login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@csrf_protect
def sign_up(request):

    signup_form = SignupForm()

    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('/dashboard')

    return render(request, 'registration/sign-up.html', context={'form': signup_form})

@csrf_protect
def change_password(request):

    if request.method == 'POST':
        change_passwd_form = PasswordChangeForm(request.user, request.POST)
        if change_passwd_form.is_valid():
            update_session_auth_hash(request, change_passwd_form.save())
        return render(request, template_name='registration/change_password.html', context={'request': request, 'form': change_passwd_form})

    return render(request, template_name='registration/change_password.html')
