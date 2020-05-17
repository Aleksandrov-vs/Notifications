from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from core.forms import SignupForm


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
