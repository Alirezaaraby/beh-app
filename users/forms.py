from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import users, Permissions


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ["name", "f_name", "username", "user_type"]


class UpdateProfileForm(forms.ModelForm):
    username = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "شماره پرسنلی"}
        ),
    )

    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام"}),
    )

    f_name = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام خانوادگی"}
        ),
    )

    class Meta:
        model = users
        fields = ["f_name", "username", "name"]

class PermissionsForm(forms.ModelForm):
    class Meta:
        model = Permissions
        fields = "__all__"

