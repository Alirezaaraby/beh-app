from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
)
from django import forms
from django.forms import ModelForm
from .models import users


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = [
            "name",
            "f_name",
            "username"
        ]


class UserLoginForm(AuthenticationForm):
    pass

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "username"  # Update label for clarity

    username = forms.CharField(widget=forms.TextInput, required=False)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password',
            'id': 'hi',
        }
    ))

class UserCompleteForm(ModelForm):
    class Meta:
        model = users
        fields = ["name", "f_name", "phone", "email", "inv_code","date_of_birth"]

class UpdateProfileForm(forms.ModelForm):
    username = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "شماره پرسنلی"}
        ),
    )

    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "شماره شاخص"}
        ),
    )

    f_name = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام خانوادگی"}
        ),
    )
    class Meta:
        model = users
        fields = ['f_name', 'username', 'name'] 