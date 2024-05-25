from django import forms
from django.contrib.auth.models import User
from .models import Assessments





class IndicatorItemsForm(forms.ModelForm):
    pid = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select", "placeholder": "انتخاب نوع شاخص"}
        ),
    )

    assessor_id = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "شماره شاخص"}
        ),
    )

    item = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام شاخص"}
        ),
    )

    min_effect = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "حداقل تأثیر"}
        ),
    )

    default_effect = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "تأثیر پیش‌فرض"}
        ),
    )

    max_effect = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "حداکثر تأثیر"}
        ),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "توضیحات"}
        ),
        required=False,  # Make description field optional
    )

    class Meta:
        model = Assessments
        fields = "__all__"
