from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Assessments(models.Model):
    pid = models.CharField(max_length=10)
    assessor_id = models.ForeignKey(User, on_delete=models.CASCADE)

    occure_date = models.CharField(max_length=25)
    occure_time = models.CharField(max_length=25)
    
    in_id = models.CharField(max_length=25)
    it_id = models.CharField(max_length=25)
    score = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    record_id = models.CharField(max_length=10)

    record_date = models.CharField(max_length=25) 
    record_time = models.CharField(max_length=50)

    current = models.CharField(max_length=10)

    forecastEffectTime = models.CharField(max_length=10)
    realeffect_time = models.CharField(max_length=10)

class Group(models.Model):
    g_code = models.CharField(max_length=10)
    description = models.TextField()

class GroupMembers(models.Model):
    pid = models.ForeignKey(User, on_delete=models.CASCADE)
    g_code = models.CharField(max_length=100)
    from_date = models.CharField(max_length=10)
    from_time = models.CharField(max_length=10)
    to_date = models.CharField(max_length=10)
    to_time = models.CharField(max_length=10)

class Overheads(models.Model):    
    p_id = models.CharField(max_length=10)
    overhead_level = models.CharField(max_length=10)
    overhead_id = models.CharField(max_length=10)