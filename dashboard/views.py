from django.shortcuts import render, redirect, get_object_or_404
from .models import Assessments
from indicators.models import Indicators, IndicatorItems
from users.models import users, Permissions
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
import jdatetime
from .forms import AssessmentsForm
from django.contrib.auth.decorators import login_required
from overheads.models import Overheads, utils
from django.db.models import OuterRef, Subquery, Max
from evaluation.models import History
from django.db.models import Q

@login_required
def index(request):
    # return redirect("dashboard")
    return render(request, "dashboard/index.html")

@login_required
def daily_evaluation_complete(request):
    assessments = Assessments.objects.filter(Q(status="عدم تایید") | Q(status="2"))
    
    return render(request, "dashboard/daily-evaluation/index.html", {"data": assessments, "current":"0"})

def get_local_time():
    utc_time = timezone.now()
    local_time = timezone.localtime(utc_time)
    
    minute_str = '{:02d}'.format(local_time.minute)
    
    return str(local_time.hour) + ":" + minute_str

@login_required
def daily_evaluation(request):
    if request.user.is_superuser:
        assessments = Assessments.objects.all()

        final_assessments = []
        for assessment in assessments:
            assessment_dict = {
                'id': assessment.id,
                'pid': assessment.pid,
                'assessor_id': assessment.assessor_id,
                'occure_date': assessment.occure_date,
                'occure_time': assessment.occure_time,
                'in_id': assessment.in_id,
                'it_id': assessment.it_id,
                'score': assessment.score,
                'status': assessment.status,
                'record_id': assessment.record_id,
                'record_date': assessment.record_date,
                'record_time': assessment.record_time,
                'current': assessment.current,
                'forecastEffectTime': assessment.forecastEffectTime,
                'realeffect_time': assessment.realeffect_time,
                'overhead_level': assessment.overhead_level,
                'description': assessment.description,
            }
            if assessment.status == "2":
                assessment_dict['editable'] = "0"
            else:
                assessment_dict['editable'] = "1"
            final_assessments.append(assessment_dict)
            
    else:
        user_id = request.user.id
        assessments = Assessments.objects.filter(Q(assessor_id=user_id) | Q(pid=user_id))
        asses_ids = Assessments.objects.values_list('id', flat=True)
        asses_ids = list(asses_ids)
        
        overheads = Overheads.objects.all()
        history = History.objects.filter(assessor_id = user_id)
        id_list = []
        final_assessments = []
        uids = []
        final_uids = []

        for assessment in assessments:
            assessment_dict = {
                'id': assessment.id,
                'pid': assessment.pid,
                'assessor_id': assessment.assessor_id,
                'occure_date': assessment.occure_date,
                'occure_time': assessment.occure_time,
                'in_id': assessment.in_id,
                'it_id': assessment.it_id,
                'score': assessment.score,
                'status': assessment.status,
                'record_id': assessment.record_id,
                'record_date': assessment.record_date,
                'record_time': assessment.record_time,
                'current': assessment.current,
                'forecastEffectTime': assessment.forecastEffectTime,
                'realeffect_time': assessment.realeffect_time,
                'overhead_level': assessment.overhead_level,
                'description': assessment.description,
            }
            id_list.append(assessment.id)
            if assessment.status == "2":
                assessment_dict['editable'] = "0"

            if assessment.assessor_id.id == user_id:
                assessment_dict['editable'] = "1"
            else:
                assessment_dict['editable'] = "0"
            
            if assessment.status == "نیازمند بررسی توسط مدیرکل":
                pass
            else:
                if assessment.status == "عدم تایید":
                    assessment_dict['editable'] = "0"
                final_uids.append(assessment.id)
                final_assessments.append(assessment_dict)

        for i in history:

            if i.uid.id in asses_ids:
                assessment = Assessments.objects.get(id = i.uid.id)
                assessment_dict = {
                    'id': assessment.id,
                    'pid': assessment.pid,
                    'assessor_id': assessment.assessor_id,
                    'occure_date': assessment.occure_date,
                    'occure_time': assessment.occure_time,
                    'in_id': assessment.in_id,
                    'it_id': assessment.it_id,
                    'score': assessment.score,
                    'status': assessment.status,
                    'record_id': assessment.record_id,
                    'record_date': assessment.record_date,
                    'record_time': assessment.record_time,
                    'current': assessment.current,
                    'forecastEffectTime': assessment.forecastEffectTime,
                    'realeffect_time': assessment.realeffect_time,
                    'overhead_level': assessment.overhead_level,
                    'description': assessment.description,
                    'editable' : "0"
                }
                if i.uid.id not in uids:
                    uids.append(i.uid.id)
                    if i.uid.id not in final_uids:
                        if i.status == "عدم تایید":
                            assessment_dict['editable'] = "0"
                        final_assessments.append(assessment_dict)

    return render(request, "dashboard/daily-evaluation/index.html", {"data": final_assessments, "current":"1"})


@login_required
def daily_evaluation_create(request):
    if request.user.is_superuser:
        overheads = users.objects.filter(is_superuser=False)
    else:
        user_ids = Overheads.objects.filter(overhead_id=request.user).values_list('pid', flat=True)
        overheads = users.objects.filter(id__in=user_ids)
        
    if request.method == 'POST':
        form = AssessmentsForm(request.POST, user_queryset=overheads)
        if form.is_valid():
            new_form = form.save(commit=False)

            utc_time = timezone.now()
            local_time = timezone.localtime(utc_time)
            
            tehran_year = local_time.year
            tehran_month = local_time.month
            tehran_day = local_time.day
            
            jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

            time = get_local_time()

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
            print(form.errors)
            messages.error(request, "تمامی فیلد ها را به درستی پر نمایید")
    else:
        form = AssessmentsForm(user_queryset=overheads)
    return render(request, 'dashboard/daily-evaluation/create.html', {'form': form, "user":request.user, "overheads": overheads})

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
    item = get_object_or_404(Assessments, pk=id)
    utc_time = timezone.now()
    local_time = timezone.localtime(utc_time)
    
    tehran_year = local_time.year
    tehran_month = local_time.month
    tehran_day = local_time.day
    
    jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

    time = get_local_time()

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

    if request.user.is_superuser:
        item.status = 2
        item.assessor_id = request.user

        item.record_date = jalili_date
        item.record_time = time

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

    else:

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
        
        
    item.save()
    return redirect('daily-evaluation')

@login_required
def daily_evaluation_modify(request, id):
    item = get_object_or_404(Assessments, pk=id)
    utc_time = timezone.now()
    local_time = timezone.localtime(utc_time)
    
    tehran_year = local_time.year
    tehran_month = local_time.month
    tehran_day = local_time.day
    
    jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

    time = get_local_time()

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

    if request.user.is_superuser:
        utc_time = timezone.now()
        local_time = timezone.localtime(utc_time)
        
        tehran_year = local_time.year
        tehran_month = local_time.month
        tehran_day = local_time.day
        
        jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

        time = get_local_time()

        overhead = Overheads.objects.filter(pid=item.pid, overhead_level=item.overhead_level - 1).first()
        
        item.overhead_level = (item.overhead_level) - 1 
        item.status = "1"

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

        time = get_local_time()

        overhead = Overheads.objects.filter(pid=item.pid, overhead_level=item.overhead_level - 1).first()
        
        item.overhead_level = (item.overhead_level) - 1 


        item.assessor_id = overhead.overhead_id
        item.record_date = jalili_date
        item.record_time = time
        
        item.save()

    return redirect('daily-evaluation')

@login_required
def daily_evaluation_reject(request, id):
    item = get_object_or_404(Assessments, pk=id)

    utc_time = timezone.now()
    local_time = timezone.localtime(utc_time)
    
    tehran_year = local_time.year
    tehran_month = local_time.month
    tehran_day = local_time.day
    
    jalili_date =  jdatetime.date.fromgregorian(day=tehran_day,month=tehran_month,year=tehran_year) 

    time = get_local_time()

    item.status = "عدم تایید"
    item.record_date=str(jalili_date)
    item.record_time=time
    
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
    user = users.objects.all()
    permissions = None
    if request.method == 'POST':
        substitute_id = request.POST.get("substitute_id")
        if substitute_id:
            try:
                permissions = Permissions.objects.get(pid_id=request.user.id)
                Permissions.objects.create(
                    pid=substitute_id,
                    daily_evaluation=permissions.daily_evaluation,
                    personnel=permissions.personnel,
                    overheads=permissions.overheads,
                    groups=permissions.groups,
                    indicators=permissions.indicators,
                    substitute=permissions.substitute,
                    logs=permissions.logs,
                    reports=permissions.reports
                )
            except Permissions.DoesNotExist:
                permissions = None

    return render(request, "dashboard/substitute/index.html", {"users": user, "permissions": permissions})


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