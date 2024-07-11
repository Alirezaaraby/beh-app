from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from users.models import users, Permissions
from .forms import SubstituteForm

def substitute(request):
    # Exclude the current user and superusers from the queryset
    users_list = users.objects.exclude(id=request.user.id).exclude(is_superuser=True)
    permissions = None

    if request.method == 'POST':
        substitute_id = request.POST.get("substitute_id")
        if substitute_id:
            try:
                substitute_user = users.objects.get(id=substitute_id)
                permissions = Permissions.objects.get(pid_id=request.user.id)

                # Use update_or_create with defaults
                Permissions.objects.update_or_create(
                    pid=substitute_user,
                    defaults={
                        'daily_evaluation': permissions.daily_evaluation,
                        'personnel': permissions.personnel,
                        'overheads': permissions.overheads,
                        'groups': permissions.groups,
                        'indicators': permissions.indicators,
                        'substitute': permissions.substitute,
                        'logs': permissions.logs,
                        'reports': permissions.reports,
                    }
                )
                messages.success(request, 'Permissions successfully copied to the substitute user.')
                return HttpResponseRedirect(request.get_full_path())  # Reload the current URL
            except Permissions.DoesNotExist:
                messages.error(request, 'No permissions found for the current user.')
            except users.DoesNotExist:
                messages.error(request, 'Substitute user does not exist.')

    return render(request, "dashboard/substitute/index.html", {"users": users_list, "permissions": permissions})

from django.http import JsonResponse

def get_user_permissions(request):
    has_perm = Permissions.objects.get(pid=request.user)
    if not has_perm.substitute:
        return HttpResponse("forbidden")
    
    user_id = request.GET.get('user_id')
    if user_id:
        user = users.objects.get(id=user_id)
        permissions = Permissions.objects.get(pid=user)
        permissions_dict = {
            'daily_evaluation': permissions.daily_evaluation,
            'personnel': permissions.personnel,
            'overheads': permissions.overheads,
            'groups': permissions.groups,
            'indicators': permissions.indicators,
            'substitute': permissions.substitute,
            'logs': permissions.logs,
            'reports': permissions.reports,
        }
        return JsonResponse({'permissions': permissions_dict})
    return JsonResponse({'permissions': {}})

