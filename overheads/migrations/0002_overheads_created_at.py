# Generated by Django 4.2.13 on 2024-06-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("overheads", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="overheads",
            name="created_at",
            field=models.CharField(default=1, max_length=100),
        ),
    ]
