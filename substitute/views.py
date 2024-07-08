# your_app/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubstituteForm
from .service.permissions_handler import PermissionHandler  # Import the service class
from users.models import users

def substitute(request):
    if request.user.is_superuser:
        users_list = users.objects.exclude(id=request.user.id).exclude(is_superuser=True)
    else:
        users_list = users.objects.all()

    if request.method == 'POST':
        substitute_id = request.POST.get("substitute_id")
        if substitute_id:
            if request.user.is_superuser:
                pid = request.POST.get("pid")
            else:
                pid = request.user.id
            handler = PermissionHandler(substitute_id=substitute_id, pid=pid)
            if handler.copy_permissions_and_save():
                messages.success(request, 'Permissions successfully copied to the substitute user.')
            else:
                messages.error(request, 'An error occurred while copying permissions.')
            return redirect(request.get_full_path())  # Reload the current URL

    return render(request, "dashboard/substitute/index.html", {"user": request.user, "users": users_list})
