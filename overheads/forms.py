from django import forms
from .models import Overheads
from users.models import users


class OverheadsForm(forms.ModelForm):
    pid = forms.ModelChoiceField(
        queryset=users.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select js-example-basic-single", "placeholder": "انتخاب پرسنل"}
        ),
    )

    overhead_level = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "سطح بالاسری"}
        ),
    )

    overhead_id = forms.ModelChoiceField(
        queryset=users.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select js-example-basic-single", "placeholder": "انتخاب بالاسری"}
        ),
    )

    approver = forms.TypedChoiceField(
        choices=((False, 'بالاسری معمولی'), (True, 'مصوب کننده')),
        coerce=lambda x: x == 'True',
        widget=forms.Select(
            attrs={"class": "form-select", "placeholder": "انتخاب تایید کننده"}
        ),
    )

    class Meta:
        model = Overheads
        fields = "__all__"