from django.shortcuts import render, redirect
from .models import Assessments
from indicators.models import Indicators, IndicatorItems
from users.models import users
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
import jdatetime
from .forms import AssessmentsForm
# Create your views here.


def index(request):
    # return redirect("dashboard")
    return render(request, "dashboard/index.html")



def daily_evaluation(request):
    data = Assessments.objects.all()
    return render(request, "dashboard/daily-evaluation/index.html", {"data": data})


def daily_evaluation_create(request):
    if request.method == 'POST':
        form = AssessmentsForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)

            utc_time = timezone.now()
            local_time = timezone.localtime(utc_time)
            
            tehran_year = local_time.year
            tehran_month = local_time.month
            tehran_day = local_time.day
            
            jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

            time = str(local_time.hour) + ":" + str(local_time.minute)

            new_form.assessor_id = request.user
            new_form.record_date = jalili_date
            new_form.record_time = time
            new_form.status = "در دست بررسی"

            # 2 : در دست بررسی
            # 1: تایید
            # 0: عدم تایید
            
            new_form.current = True

            new_form.save()
            messages.success(request, "با موفقیت ثبت شد")
        else:
            messages.error(request, "تمامی فیلد ها را به درستی پر نمایید")
    else:
        form = AssessmentsForm()
    return render(request, 'dashboard/daily-evaluation/create.html', {'form': form, "user":request.user})


def editor(request):
    return render(request, "dashboard/daily-evaluation/editor.html")

def test(request):
    return render(request, "dashboard/test.html")
def personnel(request):
    personnel = users.objects.filter(is_superuser=False)
    return render(request, "dashboard/personnel/index.html", {"users":personnel})


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

def autocomplete(request):
    if 'term' in request.GET:
        data = users.objects.filter(username__startswith = request.GET.get('term'))
        titles = list()
        for i in data:
            titles.append(i.name + " " +i.f_name + " (" + i.username + ")")
        return JsonResponse(titles, safe=False)