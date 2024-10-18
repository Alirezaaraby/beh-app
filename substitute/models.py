from django.db import models
from users.models import users
from django.core.validators import RegexValidator

date_regex = r'^\d{4}-\d{2}-\d{2}$'
time_regex = r'^([01]\d|2[0-3]):[0-5]\d$'

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

    from_date = models.CharField(
        validators=[RegexValidator(regex=date_regex, message="Date must be in the format YYYY-MM-DD")],
        max_length=10,
        null=True, blank=True
    )
    to_date = models.CharField(
        validators=[RegexValidator(regex=date_regex, message="Date must be in the format YYYY-MM-DD")],
        max_length=10,
        null=True, blank=True
    )

    from_time = models.CharField(
        validators=[RegexValidator(regex=time_regex, message="Time must be in the format HH:MM")],
        max_length=5,
        blank=True,
        null=True
    )
    to_time = models.CharField(
        validators=[RegexValidator(regex=time_regex, message="Time must be in the format HH:MM")],
        max_length=5,
        blank=True,
        null=True
    )