# Generated by Django 4.2.13 on 2024-06-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0003_delete_overheadsdashboard"),
    ]

    operations = [
        migrations.AddField(
            model_name="assessments",
            name="overhead_level",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
