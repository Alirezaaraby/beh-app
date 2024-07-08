from django import forms

from .models import Indicators, IndicatorItems


class IndicatorsForm(forms.ModelForm):
    in_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "کد نوع"}
        ),
    )

    item_type = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نوع شاخص"}
        ),
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "توضیحات", "rows" : "3"}),
        required=False
    )

    class Meta:
        model = Indicators
        fields = "__all__"


class IndicatorItemsForm(forms.ModelForm):
    in_id = forms.ModelChoiceField(
        queryset=Indicators.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select", "placeholder": "انتخاب نوع شاخص"}
        ),
    )

    it_id = forms.CharField(
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
            attrs={"class": "form-control", "placeholder": "توضیحات", "rows" : "3"}
        ),
        required=False,
    )

    class Meta:
        model = IndicatorItems
        fields = "__all__"
