from django.shortcuts import render

# Create your views here.

def groups(request):
    return render(request, "dashboard/groups/index.html")

def groups_create(request):
    return render(request, "dashboard/groups/create.html")

def group_items_create(request):
    return render(request, "dashboard/groups/items/create.html")
