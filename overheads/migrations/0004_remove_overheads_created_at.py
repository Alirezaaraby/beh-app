# Generated by Django 4.2.13 on 2024-06-08 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("overheads", "0003_alter_overheads_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="overheads",
            name="created_at",
        ),
    ]
