# Generated by Django 4.2.13 on 2024-05-23 00:41

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
            name="Group",
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
                ("g_code", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=1000)),
                ("body", models.TextField(default="3")),
            ],
        ),
        migrations.CreateModel(
            name="GroupMembers",
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
                ("from_date", models.CharField(max_length=10)),
                ("from_time", models.CharField(max_length=10)),
                ("to_date", models.CharField(max_length=10)),
                ("to_time", models.CharField(max_length=10)),
                (
                    "g_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="groups.group"
                    ),
                ),
                (
                    "pid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]