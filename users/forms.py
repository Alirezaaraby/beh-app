from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import users, Permissions


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=32,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": ""}),
    )

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام"}),
    )

    f_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام خانوادگی"}),
    )
    
    class Meta:
        model = get_user_model()
        fields = ["name", "f_name", "username"]


class UpdateProfileForm(forms.ModelForm):
    username = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "شماره پرسنلی"}
        ),
    )

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام"}),
    )

    f_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام خانوادگی"}
        ),
    )

    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور"}),
    )

    password_confirmation = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "تأیید رمز عبور"}),
    )

    class Meta:
        model = users
        fields = ["f_name", "username", "name", "password", "password_confirmation"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        if password and password != password_confirmation:
            raise forms.ValidationError("رمز عبور و تأیید رمز عبور مطابقت ندارند")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class PermissionsForm(forms.ModelForm):
    class Meta:
        model = Permissions
        fields = "__all__"

