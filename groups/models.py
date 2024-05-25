from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Groups(models.Model):
    g_code = models.CharField(max_length=10)
    name = models.CharField(max_length=500)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class GroupMembers(models.Model):
    pid = models.ForeignKey(User, on_delete=models.CASCADE)
    g_code = models.ForeignKey(Groups, on_delete=models.CASCADE)
    from_date = models.CharField(max_length=10)
    from_time = models.CharField(max_length=10)
    to_date = models.CharField(max_length=10)
    to_time = models.CharField(max_length=10)
    description = models.TextField(default="")
