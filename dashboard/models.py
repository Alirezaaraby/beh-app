from django.db import models
from users.models import users
from indicators.models import Indicators, IndicatorItems
# Create your models here.

class Assessments(models.Model):
    pid = models.ForeignKey(users, on_delete=models.CASCADE, related_name='assessments_as_pid')
    assessor_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name='assessments_as_assessor')

    occure_date = models.CharField(max_length=25)
    occure_time = models.CharField(max_length=25, blank=True, null=True)
    
    in_id = models.ForeignKey(Indicators, on_delete=models.CASCADE)
    it_id = models.ForeignKey(IndicatorItems, on_delete=models.CASCADE)
    score = models.IntegerField()
    status = models.CharField(max_length=25)
    record_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name='assessments_as_record')

    record_date = models.CharField(max_length=25) 
    record_time = models.CharField(max_length=50, blank=True, null=True)

    current = models.CharField(max_length=10, blank=True, null=True)

    forecastEffectTime = models.CharField(max_length=10, blank=True, null=True)
    realeffect_time = models.CharField(max_length=10, blank=True, null=True)

    description = models.TextField()

