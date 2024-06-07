# Generated by Django 4.2.13 on 2024-06-07 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Overheads",
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
                ("overhead_level", models.CharField(max_length=100)),
                (
                    "overhead_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="overhead_ids",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "pid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="overhead_pids",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
