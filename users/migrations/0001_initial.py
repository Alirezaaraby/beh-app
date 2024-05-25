# Generated by Django 4.2.13 on 2024-05-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="users",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50)),
                ("f_name", models.CharField(blank=True, max_length=50)),
                ("username", models.CharField(max_length=32, unique=True)),
                (
                    "phone",
                    models.CharField(blank=True, max_length=15, null=True, unique=True),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=320, null=True, unique=True
                    ),
                ),
                ("inv_code", models.CharField(blank=True, max_length=17)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "date_of_birth",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "expiration",
                    models.CharField(blank=True, default="30", max_length=3),
                ),
                (
                    "orcid",
                    models.CharField(
                        blank=True, default=None, max_length=2048, null=True
                    ),
                ),
                (
                    "g_scholar",
                    models.CharField(
                        blank=True, default=None, max_length=2048, null=True
                    ),
                ),
                (
                    "g_patent",
                    models.CharField(
                        blank=True, default=None, max_length=2048, null=True
                    ),
                ),
                ("image", models.ImageField(upload_to="static/")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]