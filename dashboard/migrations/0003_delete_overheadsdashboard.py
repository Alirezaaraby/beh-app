# Generated by Django 4.2.13 on 2024-06-07 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_overheadsdashboard_delete_overheads"),
    ]

    operations = [
        migrations.DeleteModel(
            name="OverheadsDashboard",
        ),
    ]
