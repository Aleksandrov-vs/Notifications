from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from groups.forms import GroupCreationForm
from groups.models import TelegramUser
from django.views.generic import View
from django.contrib import messages
from groups.models import Group


class DashboardGroupsView(LoginRequiredMixin, View):

    login_url = '/account/login'

    def get(self, request):
        user_groups = Group.objects.filter(manager=request.user).all()
        group_creation_form = GroupCreationForm()
        return render(request, 'dashboard/groups/groups.html',context={'form': group_creation_form, 'groups': user_groups})

    def post(self, request):
        user_groups = Group.objects.filter(manager=request.user).all()
        user = request.user
        group_creation_form = GroupCreationForm(request.POST)

        if group_creation_form.is_valid():
            group = group_creation_form.save(commit=False)
            group.manager = user
            group.save()
            user_groups = Group.objects.filter(manager=request.user).all()
            return render(request, 'dashboard/groups/groups.html', context={'form': group_creation_form, 'groups':
                user_groups})

        return render(request, 'dashboard/groups/groups.html',
                      context={'form': group_creation_form, 'groups': user_groups})


@login_required(login_url='/account/login')
def view_group(request, group_id):

    try:
        group = Group.objects.get(id=group_id)
        context = dict()
        context['group'] = group
    except Group.DoesNotExist:
        return redirect('/dashboard/groups')

    return render(request, 'dashboard/groups/group.html', context)


@login_required(login_url='/account/login')
def delete_group(request, group_id):

    try:
        group = Group.objects.get(id=group_id)
        if request.user == group.manager:
            group.delete()
            all_users = TelegramUser.objects.all()
            for user in all_users:
                if group_id in user.groups:
                    user.groups.remove(group_id)
                    user.save()
            messages.info(request, f'Вы успешно удалили группу {group.name}')

    except Group.DoesNotExist:
        pass

    return redirect('/dashboard/groups')
