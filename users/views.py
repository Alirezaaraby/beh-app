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
            return render(request, "registrations/register.html", {"form": form})
        else:
            return redirect("dashboard")
    else:
        return redirect("login")


def reset_password(request):
    pass


class UpdateProfileView(UpdateView):
    model = users
    template_name = "registrations/user_edit.html"
    form_class = UpdateProfileForm

    def get_object(self):
        return self.request.user


@login_required(login_url="/accounts/login/")
def complete_account(request):
    if request.user.is_authenticated:

        name = request.user.name
        f_name = request.user.f_name
        phone = request.user.phone
        email = request.user.email
        date_of_birth = request.user.date_of_birth
        
        if len(name) and len(f_name) and len(phone) and len(email) and len(date_of_birth) != 0:
            return redirect("dashboard")
        else:
            if request.method == "POST":
                instance = get_object_or_404(users, pk=request.user.id)
                form = UserCompleteForm(request.POST or None, instance=instance)
                if form.is_valid():
                    form.save()
                    return redirect("dashboard")

        return render(request, "registrations/complete_account.html")


@login_required(login_url="/accounts/login/")
def user_profile(request):

    if request.method == "POST":
        form = UserCompleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = UserCompleteForm()
        args = {"form": form}
        return render(request, "registrations/complete_account.html", args)

    return render(request, "profile.html", {"form": form})

from django.shortcuts import render, redirect
from .models import users
from .forms import UserProfileForm

def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            # if 'image' in request.FILES:
                # instance.image = request.FILES['image']
            
            # instance.save()
            # form.save()
            # return redirect('profile_view')  # Redirect to profile view after saving
    else:
        form = UserProfileForm(instance=user)  # Populate form with user data
    
    return render(request, 'edit_profile.html', {'form': form, "user": user})

# soal : lalezar
