# Generated by Django 4.2.13 on 2024-08-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("indicators", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="indicatoritems",
            name="it_id",
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name="indicators",
            name="in_id",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
