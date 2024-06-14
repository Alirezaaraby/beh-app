from django.shortcuts import render, redirect, get_object_or_404
from .models import Assessments
from indicators.models import Indicators, IndicatorItems
from users.models import users
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
import jdatetime
from .forms import AssessmentsForm
from django.contrib.auth.decorators import login_required
from overheads.models import Overheads
from django.db.models import OuterRef, Subquery, Max
from evaluation.models import History
from django.db.models import Q

@login_required
def index(request):
    # return redirect("dashboard")
    return render(request, "dashboard/index.html")

@login_required
def daily_evaluation(request):
    if request.user.is_superuser:
        overhead = Assessments.objects.all()
    else:
        max_overhead_level = Overheads.objects.filter(overhead_id=request.user.id).aggregate(Max('overhead_level'))
        max_level = max_overhead_level['overhead_level__max']
        
        user_id = request.user.id
        if max_level is None:
            max_level = 0

        overhead = Assessments.objects.filter(
            assessor_id=user_id,
            overhead_level__lt=int(max_level) + 1
        )


        assessments = Assessments.objects.filter(Q(assessor_id=user_id) | Q(pid=user_id))
        overhead_list = list(assessments.values())

    return render(request, "dashboard/daily-evaluation/index.html", {"data": overhead})


@login_required
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
            new_form.status = "0"
            
            new_form.current = True

            # new_form.cleaned_data['score'] = ''
            new_form.save()
            messages.success(request, "با موفقیت ثبت شد")
            return redirect("daily-evaluation-create")
        else:
            messages.error(request, "تمامی فیلد ها را به درستی پر نمایید")
    else:
        form = AssessmentsForm()
    return render(request, 'dashboard/daily-evaluation/create.html', {'form': form, "user":request.user})

@login_required
def daily_evaluation_edit(request, id):

    assesment = Assessments.objects.get(id=id)
    
    form = AssessmentsForm(instance=assesment)
    
    if request.method == "POST":
        form = AssessmentsForm(request.POST, instance=assesment)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = AssessmentsForm(instance=assesment)
    
    context = {
        'form': form
    }
    
    return render(request, 'dashboard/daily-evaluation/create.html', context)
    
@login_required
def daily_evaluation_accept(request, id):
    if request.user.is_superuser:
        item = get_object_or_404(Assessments, pk=id)       
        item.status = 2
        item.assessor_id = request.user
        
        utc_time = timezone.now()
        local_time = timezone.localtime(utc_time)
        
        tehran_year = local_time.year
        tehran_month = local_time.month
        tehran_day = local_time.day
        
        jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

        time = str(local_time.hour) + ":" + str(local_time.minute)

        item.record_date = jalili_date
        item.record_time = time

    else:

        utc_time = timezone.now()
        local_time = timezone.localtime(utc_time)
        
        tehran_year = local_time.year
        tehran_month = local_time.month
        tehran_day = local_time.day
        
        jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

        time = str(local_time.hour) + ":" + str(local_time.minute)

        item = get_object_or_404(Assessments, pk=id)
        overhead = Overheads.objects.filter(pid=item.pid, overhead_level=item.overhead_level + 1).first()
        
        item.overhead_level = item.overhead_level + 1
        
        
        # overhead = Overheads.objects.filter(pid=item.pid)

        # max_overhead_level = overhead.aggregate(Max('overhead_level'))['overhead_level__max']


        # overhead = Overheads.objects.filter(pid=item.pid)

        # max_overhead_level = overhead.aggregate(Max('overhead_level'))['overhead_level__max']

        if overhead == None:
            item.assessor_id = item.assessor_id
            item.status = "نیازمند بررسی توسط مدیرکل"
            status = item.status
        else:
            item.assessor_id = overhead.overhead_id
            if item.overhead_level == 1:
                item.status = "0"
                status = "معلق"
            elif item.overhead_level > 1:
                item.status = "1"
                status = "در دست بررسی سطح " + str(item.overhead_level)

    print(item.status)
    History.objects.create(
        pid=item.pid,
        assessor_id=item.assessor_id,
        occure_date=item.occure_date,
        occure_time=item.occure_time,
        in_id=item.in_id,
        it_id=item.it_id,
        score=item.score,
        status=item.status,
        record_id=item.record_id,
        record_date=str(jalili_date),  # Ensure date is stored as string
        record_time=time,
        current=item.current,
        forecastEffectTime=item.forecastEffectTime,
        realeffect_time=item.realeffect_time,
        description=item.description,
        uid=item
    )
        
        
    item.save()
    return redirect('daily-evaluation')

@login_required
def daily_evaluation_modify(request, id):
    if request.user.is_superuser:
        item = get_object_or_404(Assessments, pk=id)       
        utc_time = timezone.now()
        local_time = timezone.localtime(utc_time)
        
        tehran_year = local_time.year
        tehran_month = local_time.month
        tehran_day = local_time.day
        
        jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

        time = str(local_time.hour) + ":" + str(local_time.minute)

        item = get_object_or_404(Assessments, pk=id)
        overhead = Overheads.objects.filter(pid=item.pid, overhead_level=item.overhead_level - 1).first()
        
        item.overhead_level = (item.overhead_level) - 1 


        item.assessor_id = overhead.overhead_id
        item.record_date = jalili_date
        item.record_time = time
        item.save()
    else:

        utc_time = timezone.now()
        local_time = timezone.localtime(utc_time)
        
        tehran_year = local_time.year
        tehran_month = local_time.month
        tehran_day = local_time.day
        
        jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

        time = str(local_time.hour) + ":" + str(local_time.minute)

        item = get_object_or_404(Assessments, pk=id)
        overhead = Overheads.objects.filter(pid=item.pid, overhead_level=item.overhead_level - 1).first()
        
        item.overhead_level = (item.overhead_level) - 1 


        item.assessor_id = overhead.overhead_id
        item.record_date = jalili_date
        item.record_time = time
        
        item.save()

    History.objects.create(
        pid=item.pid,
        assessor_id=item.assessor_id,
        occure_date=item.occure_date,
        occure_time=item.occure_time,
        in_id=item.in_id,
        it_id=item.it_id,
        score=item.score,
        status="در دست بررسی سطح" + str(item.status),
        record_id=item.record_id,
        record_date=str(jalili_date),  # Ensure date is stored as string
        record_time=time,
        current=item.current,
        forecastEffectTime=item.forecastEffectTime,
        realeffect_time=item.realeffect_time,
        description=item.description,
        uid=item.id
    )
    return redirect('daily-evaluation')

@login_required
def daily_evaluation_reject(request, id):
    item = get_object_or_404(Assessments, pk=id)
    
    item.status = "عدم تایید"
    item.record_date=str(jalili_date)
    item.record_time=time

    utc_time = timezone.now()
    local_time = timezone.localtime(utc_time)
    
    tehran_year = local_time.year
    tehran_month = local_time.month
    tehran_day = local_time.day
    
    jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

    time = str(local_time.hour) + ":" + str(local_time.minute)
    
    History.objects.create(
        pid=item.pid,
        assessor_id=item.assessor_id,
        occure_date=item.occure_date,
        occure_time=item.occure_time,
        in_id=item.in_id,
        it_id=item.it_id,
        score=item.score,
        status="عدم تایید",
        record_id=item.record_id,
        record_date=str(jalili_date),  # Ensure date is stored as string
        record_time=time,
        current=item.current,
        forecastEffectTime=item.forecastEffectTime,
        realeffect_time=item.realeffect_time,
        description=item.description,
        uid=item
    )
    item.save()
    return redirect('daily-evaluation')

@login_required
def daily_evaluation_delete(request, id):

    item = get_object_or_404(Assessments, pk=id)
    item.delete()
    return redirect("daily-evaluation")

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
def history(request,id):
    item = History.objects.filter(uid=id)

    return render(request,"dashboard/daily-evaluation/history.html", {"history":item})