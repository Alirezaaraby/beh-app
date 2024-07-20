from django.db import models
from users.models import users
from django_jalali.db import models as jmodels

# Create your models here.

class Substitute(models.Model):
    pid = models.ForeignKey(users, on_delete=models.CASCADE, related_name='users_as_pid')
    substitute_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name='users_as_substitute')

    daily_evaluation = models.BooleanField()
    personnel = models.BooleanField()
    overheads = models.BooleanField()
    groups = models.BooleanField()
    indicators = models.BooleanField()
    substitute = models.BooleanField()
    logs = models.BooleanField()
    logs = models.BooleanField()
    reports = models.BooleanField()

    from_date = jmodels.jDateField()
    to_date= jmodels.jDateField()

