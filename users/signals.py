from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Permissions, users

@receiver(post_save, sender=users)
def create_user_permission(sender, instance, created, **kwargs):
    if created:
        Permissions.objects.create(pid=instance)
