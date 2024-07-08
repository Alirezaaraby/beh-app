from django.http import HttpResponseRedirect
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

            duplicate_exists = Overheads.objects.filter(pid=pid, overhead_id=overhead_id).exists()
            if duplicate_exists == False:
                duplicate_exists = Overheads.objects.filter(pid=pid, overhead_id=overhead_id).exists()

            if duplicate_exists:
                messages.error(request, 'بالاسری تکراری')
                return render(request, 'dashboard/overheads/modify.html', {'form': form})
            
            last_overhead_level = Overheads.objects.filter(pid=pid).first()
            if last_overhead_level == None:
                # messages.error(request, 'شماره بالاسری تکراری')
                # return render(request, 'dashboard/overheads/modify.html', {'form': form})
                pass
            
            else:
                if int(last_overhead_level.overhead_level)  + 1  < overhead_level:
                    messages.error(request, f'ترتیب را رعایت کنید')
                    return render(request, 'dashboard/overheads/modify.html', {'form': form})
                
            if overhead_level <= 0:
                messages.error(request, f'حداقل مقدار بالاسری 1 میباشد')
                return render(request, 'dashboard/overheads/modify.html', {'form': form})
            
            approver_duplicate = Overheads.objects.filter(pid=pid, approver=True).exists()
            if approver_duplicate:
                messages.error(request, 'مصوب کننده وجود دارد')
                return render(request, 'dashboard/overheads/modify.html', {'form': form})
            
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
    return HttpResponseRedirect(request.get_full_path())
def overheads_details(request, id):
    overheads = Overheads.objects.filter(pid=id)
    user_data = users.objects.get(id=id)
    return render(request, "dashboard/overheads/user.html", {"overheads": overheads, "user_data":user_data})