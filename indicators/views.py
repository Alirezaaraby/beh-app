from django.shortcuts import render, redirect, get_object_or_404
from .models import Indicators, IndicatorItems
from .forms import IndicatorsForm, IndicatorItemsForm
# Create your views here.

def indicators(request):
    indicators = Indicators.objects.all()
    indicatoritems = IndicatorItems.objects.all()
    return render(request, "dashboard/indicators/index.html", {'indicators': indicators, 'indicatoritems': indicatoritems})


def indicators_create(request):
    form = IndicatorsForm()
    if request.method == 'POST':
        form = IndicatorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indicators')
    return render(request, 'dashboard/indicators/create.html', {'form': form})

def indicator_items_create(request):
    form = IndicatorItemsForm()
    if request.method == 'POST':
        form = IndicatorItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indicators')
    return render(request, 'dashboard/indicators/items/create.html', {'form': form})

def indicators_edit(request,id):

    indicator = Indicators.objects.get(id=id)
    
    form = IndicatorsForm(instance=indicator)
    
    if request.method == "POST":
        form = IndicatorsForm(request.POST, instance=indicator)
        if form.is_valid():
            form.save()
            return redirect("indicators")
    
    context = {
        'form': form
    }
    
    return render(request, 'dashboard/indicators/edit.html', context)

def indicator_items_edit(request,id):

    indicatoritems = IndicatorItems.objects.get(id=id)
    
    form = IndicatorItemsForm(instance=indicatoritems)
    
    if request.method == "POST":
        form = IndicatorItemsForm(request.POST, instance=indicatoritems)
        if form.is_valid():
            form.save()
            return redirect("indicators")
    
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