from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('/account/login')

    return render(request, 'dashboard.html')