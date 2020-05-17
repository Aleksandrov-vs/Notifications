from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from groups.forms import GroupCreationForm
from django.contrib import messages
from groups.models import Group


@login_required(login_url='/account/login')
def dashboard_groups(request):

    user_groups = Group.objects.filter(manager=request.user).all()
    context = dict()

    if len(user_groups) == 0:
        context['no_groups'] = True
    else:
        context['groups'] = user_groups

    return render(request, 'dashboard/groups.html', context)


@login_required(login_url='/account/login')
def view_group(request, group_id):

    try:
        group = Group.objects.get(id=group_id)
        context = dict()
        context['group'] = group
    except Group.DoesNotExist:
        return redirect('/dashboard/groups')

    return render(request, 'dashboard/group.html', context)


@login_required(login_url='/account/login')
def delete_group(request, group_id):

    try:
        group = Group.objects.get(id=group_id)
        group.delete()
        messages.info(request, f'Вы успешно удалили группу {group.name}')
    except Group.DoesNotExist:
        messages.error(request, ':)')

    return redirect('/dashboard/groups')


# @login_required(login_url='/account/login')
# def add_group(request):
#
#
