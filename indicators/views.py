from django.shortcuts import render, redirect, get_object_or_404
from .models import Indicators, IndicatorItems
from .forms import IndicatorsForm, IndicatorItemsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def indicators(request):
    indicators = Indicators.objects.all()
    return render(request, "dashboard/indicators/index.html", {'indicators': indicators})


def indicators_create(request):
    form = IndicatorsForm()
    if request.method == 'POST':
        form = IndicatorsForm(request.POST)
        if form.is_valid():
            in_id = form.cleaned_data['in_id']
            duplicate = Indicators.objects.filter(in_id=in_id).exists()
            if duplicate:
                messages.error(request, 'کدشاخص  تکراری')
            else:
                form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = IndicatorsForm()
    return render(request, 'dashboard/indicators/modify.html', {'form': form})


def indicator_items(request):
    indicatoritems = IndicatorItems.objects.all()
    return render(request, "dashboard/indicators/items.html", {'indicatoritems': indicatoritems})

def indicator_items_create(request):
    form = IndicatorItemsForm()
    if request.method == 'POST':
        form = IndicatorItemsForm(request.POST)
        if form.is_valid():
            it_id = form.cleaned_data['it_id']
            duplicate = IndicatorItems.objects.filter(it_id=it_id).exists()

            if duplicate:
                messages.error(request, 'شماره شاخص تکراری')
            else:
                form.save()

            messages.success(request, 'با موفقیت ذخیره شد')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = IndicatorItemsForm()
    return render(request, 'dashboard/indicators/items/create.html', {'form': form})

def indicators_edit(request,id):

    indicator = Indicators.objects.get(id=id)
    
    form = IndicatorsForm(instance=indicator)
    
    if request.method == "POST":
        form = IndicatorsForm(request.POST, instance=indicator)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = IndicatorsForm(instance=indicator)

    context = {
        'form': form
    }
    
    return render(request, 'dashboard/indicators/modify.html', context)

def indicator_items_edit(request,id):

    indicatoritems = IndicatorItems.objects.get(id=id)
    
    form = IndicatorItemsForm(instance=indicatoritems)
    
    if request.method == "POST":
        form = IndicatorItemsForm(request.POST, instance=indicatoritems)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    
    context = {
        'form': form
    }
    
    return render(request, 'dashboard/indicators/items/edit.html', context)

def indicators_delete(request, id):

    item = get_object_or_404(Indicators, pk=id)
    item.delete()
    return redirect("indicators")

def indicator_items_delete(request, id):

    item = get_object_or_404(IndicatorItems, pk=id)
    item.delete()
    return redirect("indicators")

def indicator_details(request, id):
    indicator = get_object_or_404(Indicators, pk=id)
    indicatoritems = IndicatorItems.objects.filter(in_id_id = id)

    return render(request, "dashboard/indicators/details.html", {"indicator": indicator, "indicatoritems": indicatoritems})