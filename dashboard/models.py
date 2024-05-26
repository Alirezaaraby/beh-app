from django.db import models
from users.models import users
# Create your models here.

class Assessments(models.Model):
    pid = models.ForeignKey(users, on_delete=models.CASCADE, related_name='assessments_as_pid')
    assessor_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name='assessments_as_assessor')

    occure_date = models.CharField(max_length=25)
    occure_time = models.CharField(max_length=25, blank=True, null=True)
    
    in_id = models.CharField(max_length=25)
    it_id = models.CharField(max_length=25)
    score = models.IntegerField()
    status = models.CharField(max_length=25)
    record_id = models.CharField(max_length=10)

    record_date = models.CharField(max_length=25) 
    record_time = models.CharField(max_length=50, blank=True, null=True)

    current = models.CharField(max_length=10, blank=True, null=True)

    forecastEffectTime = models.CharField(max_length=10, blank=True, null=True)
    realeffect_time = models.CharField(max_length=10, blank=True, null=True)

    description = models.TextField()

class Overheads(models.Model):    
    p_id = models.CharField(max_length=10)
    overhead_level = models.CharField(max_length=10)
    overhead_id = models.CharField(max_length=10)