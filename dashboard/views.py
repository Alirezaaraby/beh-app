from django.shortcuts import render, redirect
from datetime import datetime
from .models import Assessments
from indicators.models import Indicators, IndicatorItems
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.


def index(request):
    # return redirect("dashboard")
    return render(request, "dashboard/index.html")


@login_required
def daily_evaluation(request):
    data = Assessments.objects.all()
    return render(request, "dashboard/daily-evaluation/index.html", {"data": data})


def daily_evaluation_create(request):

    users = User.objects.all()

    indicators = Indicators.objects.all()
    indicatoritems = IndicatorItems.objects.all()

    if request.method == "POST":
        current_datetime = datetime.now()

        date = current_datetime.strftime("%Y-%m-%d")
        time = current_datetime.strftime("%H:%M:%S")

        pid = request.POST.get("pid")

        assessor_id = request.user

        occure_date = request.POST.get("occure_date")
        occure_time = request.POST.get("occure_time")
        in_id = request.POST.get("in_id")
        it_id = request.POST.get("it_id")
        score = request.POST.get("score")
        record_id = request.POST.get("record_id")

        record_date = date
        record_time = time
        status = "در انتظار تایید"
        current = 1

        forecast_effect_time = request.POST.get("forecast_effect_time")
        real_effect_time = request.POST.get("real_effect_time")

        assessment = Assessments(
            pid=pid,
            assessor_id=assessor_id,
            occure_date=occure_date,
            occure_time=occure_time,
            in_id=in_id,
            it_id=it_id,
            score=score,
            status=status,
            record_id=record_id,
            record_date=record_date,
            record_time=record_time,
            current=current,
            forecastEffectTime=forecast_effect_time,
            realeffect_time=real_effect_time,
        )
        assessment.save()
        # return redirect("dashboard")
    return render(
        request,
        "dashboard/daily-evaluation/create.html",
        {"user": request.user ,"users": users, "indicators": indicators, "indicatoritems": indicatoritems},
    )


def editor(request):
    return render(request, "dashboard/daily-evaluation/editor.html")


def personnel(request):
    return render(request, "dashboard/personnel/index.html")


def substitute(request):
    return render(request, "dashboard/substitute/index.html")


def logs(request):
    return render(request, "dashboard/logs/index.html")


def reports(request):
    return render(request, "dashboard/reports/index.html")

def load_indicator_items(request):
    in_id = request.GET.get("in_id")
    indicatorItems = IndicatorItems.objects.filter(in_id=in_id).values("id", "item")
    indicator_Items_list = list(indicatorItems)
    return JsonResponse(indicator_Items_list, safe=False)

def load_indicator_item_range(request):
    it_id = request.GET.get("it_id")

    indicatorItem = IndicatorItems.objects.filter(id=it_id).values("default_effect", "min_effect", "max_effect")

    indicatorItem_list = list(indicatorItem)
    return JsonResponse(indicatorItem_list, safe=False)