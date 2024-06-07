from django.db import models
from users.models import users
# Create your models here.



class Overheads(models.Model):
    pid = models.ForeignKey(users, related_name='overhead_pids', on_delete=models.CASCADE)
    overhead_level = models.CharField(max_length=100)
    overhead_id = models.ForeignKey(users, related_name='overhead_ids', on_delete=models.CASCADE)
    created_at = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.overhead_level} - {self.pid.username}'
