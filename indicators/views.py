from django.shortcuts import render, redirect
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
            return redirect('home')
    return render(request, 'dashboard/indicators/create.html', {'form': form})

def indicator_items_create(request):
    form = IndicatorItemsForm()
    if request.method == 'POST':
        form = IndicatorItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'dashboard/indicators/items/create.html', {'form': form})