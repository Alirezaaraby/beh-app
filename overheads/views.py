from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import users
from .models import Overheads
from .forms import OverheadsForm
from django.contrib import messages
from .models import Overheads, utils
# Create your views here.

def overheads(request):
    data = users.objects.all()
    return render(request, "dashboard/overheads/index.html", {"data":data})

def overheads_create(request):
    if request.method == 'POST':
        form = OverheadsForm(request.POST)
        if form.is_valid():
                        
            pid = form.cleaned_data['pid']
            overhead_id = form.cleaned_data['overhead_id']

            overhead_level = int(form.cleaned_data['overhead_level'])

            print(pid)
            print(overhead_id)
            print(overhead_level)

            utils.objects.create(pid=pid, overhead_id=overhead_id)

            form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = OverheadsForm()
    return render(request, 'dashboard/overheads/modify.html', {'form': form})

def overheads_edit(request, id):
    overhead = Overheads.objects.get(id=id)
    
    form = OverheadsForm(instance=overhead)
    
    if request.method == "POST":
        form = OverheadsForm(request.POST, instance=overhead)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت ذخیره شد')
        else:
            messages.error(request, 'داده ها به درستی ذخیره نشدند')
    else:
        form = OverheadsForm(instance=overhead)

    context = {
        'form': form
    }
    
    return render(request, 'dashboard/overheads/modify.html', context)

@login_required
def overheads_delete(request, id):

    item = get_object_or_404(Overheads, pk=id)
    item.delete()
    return redirect("overheads")
def overheads_details(request, id):
    overheads = Overheads.objects.filter(pid=id)
    user_data = users.objects.get(id=id)
    return render(request, "dashboard/overheads/user.html", {"overheads": overheads, "user_data":user_data})
