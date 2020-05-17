from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from groups.forms import GroupCreationForm
from django.contrib import messages
from groups.models import Group
from users.models import User


@login_required(login_url='/account/login')
def dashboard_groups(request):
    context_form = dict()
    context = dict()

    if request.method == 'POST':
        context_form['form'] = add_group(request)

    user_groups = Group.objects.filter(manager=request.user).all()

    if len(user_groups) == 0:
        context['no_groups'] = True
    else:
        context['groups'] = user_groups

    context.update(context_form)
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
        if request.user == group.manager:
            group.delete()
            messages.info(request, f'Вы успешно удалили группу {group.name}')
        else:
            messages.error(request, ':)')

    except Group.DoesNotExist:
        messages.error(request, ':)')

    return redirect('/dashboard/groups')


@login_required(login_url='/account/login')
def add_group(request):

    user = request.user

    if request.method == "POST":
        group_creation_form = GroupCreationForm(request.POST)
        if group_creation_form.is_valid():
            response = group_creation_form.save(commit=False)
            response.manager = user
            response.save()

    return group_creation_form
