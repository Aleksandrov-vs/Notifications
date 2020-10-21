from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ChangePasswordMixin(View):
    bound_form = object
    templates = ''

    def get(self, request):
        return render(request, 'registration/change_password.html', {'form': self.bound_form(request.user)})

    def post(self, request):
        form = self.bound_form(request.user, request.Post)
        if form.is_valid():
            update_session_auth_hash(request, form.save())
        return render(request, 'registration/change_password.html',
                      context={'request': request, 'form': form})