from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from users.models import users, Permissions
from .models import Substitute

def substitute(request):
    # Exclude the current user and superusers from the queryset
    users_list = users.objects.exclude(id=request.user.id).exclude(is_superuser=True)
    permissions = None

    if request.method == "POST":
        substitute_id = request.POST.get("substitute_id")
        pid = request.POST.get("pid")
        daily_evaluation = bool(request.POST.get("daily_evaluation"))
        personnel = bool(request.POST.get("personnel"))
        overheads = bool(request.POST.get("overheads"))
        groups = bool(request.POST.get("groups"))
        indicators = bool(request.POST.get("indicators"))
        substitute = bool(request.POST.get("substitute"))
        logs = bool(request.POST.get("logs"))
        reports = bool(request.POST.get("reports"))
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")
        from_time = request.POST.get("from_time")
        to_time = request.POST.get("to_time")

        if substitute_id:
            if pid == substitute_id:
                messages.error(request, "کاربر و جانشین یکسان میباشند")
            else:
                try:
                    substitute_user = users.objects.get(id=substitute_id)
                    pid_user = users.objects.get(id=pid)
                    permissions = Permissions.objects.get(pid_id=request.user.id)

                    # Use update_or_create with defaults
                    Permissions.objects.update_or_create(
                        pid=substitute_user,
                        defaults={
                            "daily_evaluation": permissions.daily_evaluation,
                            "personnel": permissions.personnel,
                            "overheads": permissions.overheads,
                            "groups": permissions.groups,
                            "indicators": permissions.indicators,
                            "substitute": permissions.substitute,
                            "logs": permissions.logs,
                            "reports": permissions.reports,
                        },
                    )
                    print(from_date)
                    if to_date == "":
                        to_date = None
                    if from_time == "":
                        from_time = None
                    if to_time == "":
                        to_time = None
                    substitute_instance = Substitute(
                        pid=pid_user,
                        substitute_id=substitute_user,
                        daily_evaluation=daily_evaluation,
                        personnel=personnel,
                        overheads=overheads,
                        groups=groups,
                        indicators=indicators,
                        substitute=substitute,
                        logs=logs,
                        reports=reports,
                        from_date=from_date,
                        to_date=to_date,
                    )

                    substitute_instance.save()

                    messages.success(
                        request,
                        "جانشین با موفقیت انتخاب شد. تغییرات برای کاربر جانشین اعمال شد.",
                    )
                    return HttpResponseRedirect(
                        request.get_full_path()
                    )
                except Permissions.DoesNotExist:
                    messages.error(
                        request, "No permissions found for the current user."
                    )
                except users.DoesNotExist:
                    messages.error(request, "Substitute user does not exist.")

    return render(request, "dashboard/substitute/index.html", {"users": users_list})

def get_user_permissions(request):
    has_perm = Permissions.objects.get(pid=request.user)
    if not has_perm.substitute:
        return HttpResponse("forbidden")

    user_id = request.GET.get("user_id")
    if user_id:
        user = users.objects.get(id=user_id)
        permissions = Permissions.objects.get(pid=user)
        permissions_dict = {
            "daily_evaluation": permissions.daily_evaluation,
            "personnel": permissions.personnel,
            "overheads": permissions.overheads,
            "groups": permissions.groups,
            "indicators": permissions.indicators,
            "substitute": permissions.substitute,
            "logs": permissions.logs,
            "reports": permissions.reports,
        }
        return JsonResponse({"permissions": permissions_dict})
    return JsonResponse({"permissions": {}})
