# Generated by Django 4.2.13 on 2024-06-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OverheadsDashboard",
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
                ("p_id", models.CharField(max_length=10)),
                ("overhead_level", models.CharField(max_length=10)),
                ("overhead_id", models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name="Overheads",
        ),
    ]
