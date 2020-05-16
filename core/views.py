from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from core.forms import FormReg as f
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from users.models import User
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('/account/login')

    return render(request, 'dashboard.html')

@csrf_protect
def sing_up(request):
    if request.method == 'POST':
        user_form = f(request.POST)
        print(user_form.instance)
        if user_form.is_valid():
            user_form.save()
            new_user =user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            print('aaaaa', user_form.instance)
            return redirect('/dashboard', context = User)
        else:
            print(user_form.errors)
    else:
        user_form = f()
    return render(request, template_name='registration/registration.html', context={'form': user_form})