from django import forms
from .models import Groups, GroupMembers
from users.models import users


class GroupsForm(forms.ModelForm):
    g_code = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "کد گروه"}
        ),
    )

    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "عنوان گروه"}
        ),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "توضیحات", "rows" : "3"}
        ),
        required=False,
    )

    class Meta:
        model = Groups
        fields = "__all__"


class GroupMembersForm(forms.ModelForm):
    pid = forms.ModelChoiceField(
        queryset=users.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select js-example-basic-single", "placeholder": "انتخاب نوع شاخص"}
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
        required=False
    )

    to_time = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام شاخص"}
        ),
        required=False
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "توضیحات", "rows" : "3"}
        ),
        required=False,
    )

    class Meta:
        model = GroupMembers
        fields = "__all__"
