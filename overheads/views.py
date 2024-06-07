from django.shortcuts import render, redirect
from users.models import users
from .forms import OverheadsForm
# Create your views here.

def overheads(request):
    pass

def overheads_create(request):
    if request.method == 'POST':
        form = OverheadsForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message or redirect to another page
            return redirect('overheads')  # Change to your success URL
    else:
        form = OverheadsForm()
    return render(request, 'dashboard/overheads/modify.html', {'form': form})