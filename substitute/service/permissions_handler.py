# your_app/service/permissions_handler.py

from users.models import users, Permissions
from substitute.models import Substitute

class PermissionHandler:
    def __init__(self, substitute_id, pid):
        self.substitute_id = substitute_id
        self.pid = pid

    def copy_permissions_and_save(self):
        try:
            substitute_user = users.objects.get(id=self.substitute_id)
            permissions = Permissions.objects.get(pid_id=self.pid)

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

            # Save the substitute relationship
            Substitute.objects.create(pid=users.objects.get(id=self.pid), substitute_id=substitute_user)

            return True

        except users.DoesNotExist:
            print('User does not exist')
            return False
        except Permissions.DoesNotExist:
            print('Permissions do not exist for the user')
            return False

        return False
