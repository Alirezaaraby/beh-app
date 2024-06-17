# Generated by Django 4.2.13 on 2024-06-16 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("overheads", "0004_remove_overheads_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="utils",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "overhead_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="overheads_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "pid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="overheads_pid",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]