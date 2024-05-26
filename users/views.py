from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UpdateProfileForm
from django.contrib import messages
from .models import users
from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = UserRegistrationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.error(request, form.errors)
            else:
                form = UserRegistrationForm()
            return render(request, "registration/register.html", {"form": form})
        else:
            return redirect("dashboard")
    else:
        return redirect("login")


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


def delete(request, id):
    user = get_object_or_404(users, pk=id)
    user.delete()
    return redirect("personnel")
