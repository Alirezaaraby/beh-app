from django.db import models
from users.models import users
# Create your models here.

class Substitute(models.Model):
    pid = models.ForeignKey(users, on_delete=models.CASCADE, related_name='users_as_pid')
    substitute_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name='users_as_substitute')
