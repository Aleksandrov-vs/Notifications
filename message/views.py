from django.contrib.auth.mixins import LoginRequiredMixin
from message.forms import MessageCreationForm
from django.views.generic import View
from django.shortcuts import render
from message.models import Message
from groups.models import Group


class DashboardMessagesView(LoginRequiredMixin, View):

    login_url = '/account/login'

    def get(self, request):

        notifications = Message.objects.filter(group__manager=request.user).all()
        message_creation_form = MessageCreationForm(request.user)
        groups = Group.objects.filter(manager=request.user)
        return render(request, 'dashboard/messages/messages.html', context={'notifications': notifications,
                                                                            'groups': groups,
                                                                            'form': message_creation_form})

    def post(self, request):

        notifications = Message.objects.filter(group__manager=request.user).all()
        message_creation_form = MessageCreationForm(request.user, request.POST)
        selected_group = message_creation_form.data.get('group')

        try:
            if message_creation_form.is_valid():
                if Group.objects.get(id=selected_group).manager == request.user:
                    message_creation_form.save()
        except Group.DoesNotExist:
            pass

        return render(request, 'dashboard/messages/messages.html', context={'notifications': notifications,
                                                                            'form': message_creation_form})