from django.shortcuts import render

# Create your views here.

def index(request):
    # return redirect("dashboard")
    return render(request,"dashboard/index.html")

def daily_evaluation(request):
    return render(request, "dashboard/daily-evaluation/index.html")

def daily_evaluation_create(request):
    return render(request, "dashboard/daily-evaluation/create.html")
def editor(request):
    return render(request, "dashboard/daily-evaluation/editor.html")

def editor(request):
    return render(request, "dashboard/daily-evaluation/editor.html")

def personnel(request):
    return render(request, "dashboard/personnel/index.html")

def groups(request):
    return render(request, "dashboard/groups/index.html")

def indicators(request):
    return render(request, "dashboard/indicators/index.html")

def substitute(request):
    return render(request, "dashboard/substitute/index.html")

def logs(request):
    return render(request, "dashboard/logs/index.html")

def reports(request):
    return render(request, "dashboard/reports/index.html")