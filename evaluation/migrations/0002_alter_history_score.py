# Generated by Django 4.2.13 on 2024-06-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="history",
            name="score",
            field=models.CharField(max_length=250),
        ),
    ]
