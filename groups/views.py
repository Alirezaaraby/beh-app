from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Groups, GroupMembers
from .forms import GroupsForm, GroupMembersForm
# Create your views here.

def groups(request):
    groups = Groups.objects.all()
    groupmembers = GroupMembers.objects.all()
    return render(request, "dashboard/groups/index.html", {'groups': groups, 'groupmembers': groupmembers})

def groups_create(request):
    form = GroupsForm()
    if request.method == 'POST':
        form = GroupsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
            # return redirect('groups')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = GroupsForm()
    return render(request, 'dashboard/groups/modify.html', {'form': form})

def group_members_create(request):
    form = GroupMembersForm()
    if request.method == 'POST':
        form = GroupMembersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
            # return redirect('groups')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = GroupMembersForm()
    return render(request, 'dashboard/groups/members/index.html', {'form': form})

def groups_edit(request, id):
    group = get_object_or_404(Groups, id=id)
    
    if request.method == "POST":
        form = GroupsForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = GroupsForm(instance=group)
    
    context = {
        'form': form
    }
    
    return render(request, 'dashboard/groups/modify.html', context)

def group_members_edit(request,id):

    groupmembers = GroupMembers.objects.get(id=id)
    
    form = GroupMembersForm(instance=groupmembers)
    
    if request.method == "POST":
        form = GroupMembersForm(request.POST, instance=groupmembers)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = GroupMembersForm(instance=groupmembers)
    
    context = {
        'form': form
    }
    
    return render(request, 'dashboard/groups/members/index.html', context)

def groups_delete(request, id):

    item = get_object_or_404(Groups, pk=id)
    item.delete()
    return redirect("groups")

def group_members_delete(request, id):

    item = get_object_or_404(GroupMembers, pk=id)
    item.delete()
    return redirect("groups")