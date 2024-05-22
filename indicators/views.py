from django.shortcuts import render

# Create your views here.

def indicators(request):
    return render(request, "dashboard/indicators/index.html")


def indicators_create(request):
    return render(request, "dashboard/indicators/create.html")

def indicator_items_create(request):
    return render(request, "dashboard/indicators/items/create.html")