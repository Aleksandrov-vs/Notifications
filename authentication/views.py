from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from authentication.forms import SignupForm, ChangePasswordForm
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



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




class ChangePasswordViews(LoginRequiredMixin, View):
    login_url = '/account/login'

    def get(self, request):
        change_pswd_form = ChangePasswordForm(request.user)
        return render(request, 'registration/change_password.html', {'form': change_pswd_form})

    def post(self, request):
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            update_session_auth_hash(request, form.save())
        return render(request, 'registration/change_password.html',
                      context={'request': request, 'form': form})
