from django.db import models

# Create your models here.
class Indicators(models.Model):
    in_id = models.CharField(max_length=10)
    item_type = models.CharField(max_length=250)

class IndicatorItems(models.Model):    
    in_id = models.CharField(max_length=25)
    it_id = models.CharField(max_length=25)
    item = models.CharField(max_length=25)
    min_effect = models.CharField(max_length=25)
    default_effect = models.CharField(max_length=25)
    max_efect = models.CharField(max_length=25)