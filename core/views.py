from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from core.forms import FormReg as f
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from users.models import User


def index(request):
    return render(request, 'index.html')


def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('/account/login')

    return render(request, 'dashboard.html')

@csrf_protect
def sing_up(request):
    if request.method == 'POST':
        formUser = f(request.POST)
        if formUser.is_valid():
            formUser.save()
            NewUser = User
            User.save(formUser.instance)
        return render(request, template_name='registration/registration.html', context={'form': formUser})
    return render(request, template_name='registration/registration.html', context={'registered': False})