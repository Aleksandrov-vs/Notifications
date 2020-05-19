from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from authentication.forms import SignupForm
from django.contrib.auth import login


@csrf_protect
def sign_up(request):

    if request.user.is_authenticated:
        return redirect('/dashboard')

    signup_form = SignupForm()

    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('/dashboard')

    return render(request, 'registration/sign-up.html', context={'form': signup_form})


@csrf_protect
@login_required(login_url='/account/login')
def change_password(request):

    if request.method == 'POST':
        change_pswd_form = PasswordChangeForm(request.user, request.POST)
        if change_pswd_form.is_valid():
            update_session_auth_hash(request, change_pswd_form.save())
        return render(request, 'registration/change_password.html', context={'request': request, 'form': change_pswd_form})

    return render(request, 'registration/change_password.html')