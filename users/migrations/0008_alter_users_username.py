# Generated by Django 4.2.13 on 2024-10-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_permissions_daily_evaluation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="username",
            field=models.IntegerField(unique=True),
        ),
    ]
