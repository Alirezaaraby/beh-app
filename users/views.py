from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserCompleteForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from .models import users
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import users

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("complete")
        else:
            return render(
                request, "login.html", {"error": "Invalid email or password."}
            )
    else:
        return render(request, "login.html")


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
            return redirect("register")
    else:
        return redirect("register")


def reset_password(request):
    pass

def edit(request, id):
    user = get_object_or_404(users, pk=id)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UpdateProfileForm(instance=user)
    return render(request, "dashboard/personnel/edit.html", {"form": form, "user": user})

def profile(request):
    pass

def delete(request, id):
    user = get_object_or_404(users, pk=id)
    user.delete()
    return redirect("personnel")