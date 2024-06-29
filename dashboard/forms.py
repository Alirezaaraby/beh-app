# forms.py

from django import forms
from .models import Assessments
from users.models import users
from indicators.models import Indicators, IndicatorItems
from overheads.models import utils

MONTH_CHOICES = [
    (1, "فروردین"),
    (2, "اردیبهشت"),
    (3, "خرداد"),
    (4, "تیر"),
    (5, "مرداد"),
    (6, "شهریور"),
    (7, "مهر"),
    (8, "آبان"),
    (9, "آذر"),
    (10, "دی"),
    (11, "بهمن"),
    (12, "اسفند"),
]


class AssessmentsForm(forms.ModelForm):
    pid = forms.ModelChoiceField(
        queryset=users.objects.none(),
        widget=forms.Select(
            attrs={"class": "form-select js-example-basic-single", "placeholder": "ارزیابی شونده", "id": "pid"}
        ),
    )
    in_id = forms.ModelChoiceField(
        queryset=Indicators.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select js-example-basic-single1", "placeholder": "نوع شاخص", "id": "in_id"}
        ),
    )
    it_id = forms.ModelChoiceField(
        queryset=IndicatorItems.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select", "placeholder": "شاخص", "id": "it_id"}
        ),
    )
    score = forms.CharField(
        max_length=250,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "امتیاز", "id": "score"}
        ),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "توضیحات", "id": "description"}
        ),
        required=True,
    )
    record_id = forms.ModelChoiceField(
        queryset=users.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-select js-example-basic-single", "placeholder": "شماره پرسنلی ثبت کننده", "id": "record_id"}
        ),
    )
    occure_date = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "تاریخ وقوع", "id": "occure_date", "data-jdp": ""}
        ),
    )
    forecastEffectTime = forms.ChoiceField(
        choices=MONTH_CHOICES,
        required=True,
        label="پیش بینی زمان تاثیر",
        widget=forms.Select(
            attrs={"class": "form-select", "id": "forecastEffectTime", "placeholder": "پیش بینی زمان تاثیر"}),
    )

    class Meta:
        model = Assessments
        fields = [
            "pid",
            "in_id",
            "it_id",
            "score",
            "description",
            "record_id",
            "occure_date",
            "forecastEffectTime",
        ]

    def __init__(self, *args, **kwargs):
        user_queryset = kwargs.pop('user_queryset', users.objects.none())
        super(AssessmentsForm, self).__init__(*args, **kwargs)
        self.fields['pid'].queryset = user_queryset

