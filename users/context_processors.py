from .models import Permissions
from django.shortcuts import get_object_or_404

def add_permissions(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            permissions = {
                'daily_evaluation': True,
                'personnel': True,
                'overheads': True,
                'groups': True,
                'indicators': True,
                'substitute': True,
                'logs': True,
                'reports': True,
            }
        else:
            permissions = get_object_or_404(Permissions, pid=request.user)
    else:
        permissions = None
        
    return {'menu_permissions': permissions}
