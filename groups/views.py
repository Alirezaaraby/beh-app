from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('groups')
    return render(request, 'dashboard/groups/create.html', {'form': form})

def group_members_create(request):
    form = GroupMembersForm()
    if request.method == 'POST':
        form = GroupMembersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    return render(request, 'dashboard/groups/members/create.html', {'form': form})

def groups_edit(request,id):

    group = Groups.objects.get(id=id)
    
    form = GroupsForm(instance=group)
    
    if request.method == "POST":
        form = GroupsForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("groups")
    
    context = {
        'form': form
    }
    
    return render(request, 'dashboard/groups/edit.html', context)

def group_members_edit(request,id):

    groupmembers = GroupMembers.objects.get(id=id)
    
    form = GroupMembersForm(instance=groupmembers)
    
    if request.method == "POST":
        form = GroupMembersForm(request.POST, instance=groupmembers)
        if form.is_valid():
            form.save()
            return redirect("groups")
    
    context = {
        'form': form
    }
    
    return render(request, 'dashboard/groups/members/edit.html', context)

def groups_delete(request, id):

    item = get_object_or_404(Groups, pk=id)
    item.delete()
    return redirect("groups")

def group_members_delete(request, id):

    item = get_object_or_404(GroupMembers, pk=id)
    item.delete()
    return redirect("groups")