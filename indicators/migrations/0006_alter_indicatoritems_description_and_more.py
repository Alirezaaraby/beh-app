# Generated by Django 4.2.13 on 2024-05-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("indicators", "0005_alter_indicatoritems_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="indicatoritems",
            name="description",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="indicators",
            name="description",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]