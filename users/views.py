from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UpdateProfileForm, PermissionsForm
from django.contrib import messages
from .models import users, Permissions
from django.contrib.auth.decorators import login_required
from .decorators import superuser_required

@superuser_required
def register(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = UserRegistrationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "با موفقیت ایجاد شد")
                else:
                    messages.error(request, form.errors)
            else:
                form = UserRegistrationForm()
            return render(request, "registration/register.html", {"form": form})
        else:
            return redirect("dashboard")
    else:
        return redirect("login")

@superuser_required
def edit(request, id):
    user = get_object_or_404(users, pk=id)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UpdateProfileForm(instance=user)
    return render(
        request, "dashboard/personnel/edit.html", {"form": form, "user": user}
    )

@superuser_required
def delete(request, id):
    user = get_object_or_404(users, pk=id)
    user.delete()
    return redirect("personnel")

@superuser_required
def permissions(request, id):
    user_instance = get_object_or_404(users, id=id)
    p, created = Permissions.objects.get_or_create(pid=user_instance)
    
    if request.method == 'POST':
        
        p.daily_evaluation = request.POST.get('daily_evaluation')
        p.personnel = request.POST.get('personnel')
        p.overheads = request.POST.get('overheads')
        p.groups = request.POST.get('groups')
        p.indicators = request.POST.get('indicators')
        p.substitute = request.POST.get('substitute')
        p.logs = request.POST.get('logs')
        p.reports = request.POST.get('reports')

        p.save()
        return redirect("personnel")
    
    return render(request, "dashboard/personnel/permissions.html", {"permissions": p,"permission_id": id})