from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from groups.forms import GroupCreationForm
from groups.models import TelegramUser
from django.contrib import messages
from groups.models import Group
from django.views.generic import View


# @login_required(login_url='/account/login')
# def dashboard_groups(request):
#
#     context_form = dict()
#     context = dict()
#
#     if request.method == 'POST':
#         context_form['form'] = add_group(request)
#
#     user_groups = Group.objects.filter(manager=request.user).all()
#
#     if len(user_groups) == 0:
#         context['no_groups'] = True
#     else:
#         context['groups'] = user_groups
#
#     context.update(context_form)
#     return render(request, 'dashboard/groups/groups.html', context)

# @login_required(login_url='/account/login')
# def add_group(request):
#
#     group_creation_form = GroupCreationForm()
#     user = request.user
#
#     if request.method == "POST":
#         group_creation_form = GroupCreationForm(request.POST)
#         if group_creation_form.is_valid():
#             group = group_creation_form.save(commit=False)
#             group.manager = user
#             group.save()
#
#     return group_creation_form


class DashboardGroupsView(View):
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
            return render(request, 'dashboard/groups/groups.html',
                          context={'form': group_creation_form, 'groups': user_groups})

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
