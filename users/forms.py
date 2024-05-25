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
        print(get_user_model())
        fields = [
     
            "username",
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
    class Meta:
        model = users
        fields = ['f_name', 'username', 'date_of_birth', 'inv_code', 'phone', 'email']

from django import forms
from .models import users

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = users
        exclude = ['password', 'is_staff', 'is_superuser', 'is_active', 'expiration', 'last_login'] 