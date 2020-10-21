from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from groups.forms import GroupCreationForm
from groups.models import TelegramUser
from django.views.generic import View
from django.contrib import messages
from groups.models import Group
from rest_framework.views import APIView


class DashboardGroupsView(LoginRequiredMixin, APIView):

    login_url = '/account/login'

    def get(self, request):

        user_groups = Group.objects.filter(manager=request.user).all()
        group_creation_form = GroupCreationForm()
        print(type(user_groups), user_groups)
        return render(request, 'dashboard/groups/groups.html',context={'form': group_creation_form, 'groups': user_groups})

    def post(self, request):

        user_groups = Group.objects.filter(manager=request.user).all()
        user = request.user
        group_creation_form = GroupCreationForm(request.POST)
        print(type(user_groups), user_groups)
        if group_creation_form.is_valid():
            group = group_creation_form.save(commit=False)
            group.manager = user
            group.save()
            user_groups = Group.objects.filter(manager=request.user).all()
            return render(request, 'dashboard/groups/groups.html', context={'form': group_creation_form, 'groups':
                user_groups})

        return render(request, 'dashboard/groups/groups.html',
                      context={'form': group_creation_form, 'groups': user_groups})


class ViewGroupView(LoginRequiredMixin, View):

    login_url = '/account/login'

    def get(self, request, group_id):

        group = Group.objects.get(id=group_id)

        if request.user == group.manager:

            try:
                group = Group.objects.get(id=group_id)
                context = dict()
                context['group'] = group
            except Group.DoesNotExist:
                return redirect('/dashboard/groups')

            list_user = list()
            all_users = TelegramUser.objects.all()

            for user in all_users:
                if group_id in user.groups:
                    list_user.append(user)

            context.update({'user_group': list_user})
            return render(request, 'dashboard/groups/group.html', context)
        else:
            return redirect('/dashboard/groups')


class DeleteGroupView(LoginRequiredMixin, View):

    login_url = '/account/login'

    def get(self, request, group_id):

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
            return redirect('/dashboard/groups')

        return redirect('/dashboard/groups')





class DeleteUser(View):

    def get(self, request, group_id, telegram_user_id):
        group = Group.objects.get(id=group_id)
        telegram_user = TelegramUser.objects.get(id=telegram_user_id)


        if request.user == group.manager:
            if group_id in telegram_user.groups:
                telegram_user.groups.remove(group_id)
                telegram_user.save()
            messages.info(request, f'Вы успешно удалили юзера {telegram_user.id}')
            return redirect(f'/dashboard/group/{group_id}')
        return redirect(f'/dashboard/group/{group_id}')
