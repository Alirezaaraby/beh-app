from django import forms
from .models import Groups, GroupMembers
from django.contrib.auth.models import User


class GroupsForm(forms.ModelForm):
    g_code = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام نوع شاخص"}
        ),
    )

    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "شماره نوع شاخص"}
        ),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "توضیحات"}
        ),
        required=False,
    )

    class Meta:
        model = Groups
        fields = "__all__"


class GroupMembersForm(forms.ModelForm):
    pid = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select", "placeholder": "انتخاب نوع شاخص"}
        ),
    )

    g_code = forms.ModelChoiceField(
        queryset=Groups.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select", "placeholder": "انتخاب نوع شاخص"}
        ),
    )

    from_date = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "شماره شاخص", "data-jdp": ""}
        ),
    )

    from_time = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام شاخص"}
        ),
    )

    to_date = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "شماره شاخص", "data-jdp":""}
        ),
    )

    to_time = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام شاخص"}
        ),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "توضیحات"}
        ),
        required=False,
    )

    class Meta:
        model = GroupMembers
        fields = "__all__"
