from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Group(models.Model):
    g_code = models.CharField(max_length=10)
    name = models.CharField(max_length=1000)

    body = models.TextField(default="3")

class GroupMembers(models.Model):
    pid = models.ForeignKey(User, on_delete=models.CASCADE)
    g_code = models.ForeignKey(Group, on_delete=models.CASCADE)
    from_date = models.CharField(max_length=10)
    from_time = models.CharField(max_length=10)
    to_date = models.CharField(max_length=10)
    to_time = models.CharField(max_length=10)