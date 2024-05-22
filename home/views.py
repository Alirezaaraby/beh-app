from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    # return redirect("dashboard")
    return render(request,"dashboard/daily.html")