from django.db import models

# Create your models here.
class Indicators(models.Model):
    in_id = models.CharField(max_length=10)
    item_type = models.CharField(max_length=500)
    description = models.TextField(default='', blank=True, null=True)
    def __str__(self):
        return self.item_type
class IndicatorItems(models.Model):    
    in_id = models.ForeignKey(Indicators, on_delete=models.CASCADE)  
    it_id = models.CharField(max_length=25)
    item = models.CharField(max_length=500)
    min_effect = models.IntegerField()  # Changed to IntegerField
    default_effect = models.IntegerField()  # Changed to IntegerField
    max_effect = models.IntegerField(default=0)  # Changed to IntegerField
    description = models.TextField(default='', blank=True, null=True)  # Changed default to a string