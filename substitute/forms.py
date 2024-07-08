# forms.py

from django import forms
from users.models import users
from .models import Substitute


class SubstituteForm(forms.ModelForm):
    substitute_id = forms.ModelChoiceField(
        queryset=users.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select js-example-basic-single", "placeholder": "ارزیابی شونده", "id": "pid"}
        ),
    )

    class Meta:
        model = Substitute
        fields = ["substitute_id"]