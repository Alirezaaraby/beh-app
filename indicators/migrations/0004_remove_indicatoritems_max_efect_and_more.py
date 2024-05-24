# Generated by Django 4.2.13 on 2024-05-24 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("indicators", "0003_indicators_description_alter_indicators_item_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="indicatoritems",
            name="max_efect",
        ),
        migrations.AddField(
            model_name="indicatoritems",
            name="max_effect",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="indicatoritems",
            name="default_effect",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="indicatoritems",
            name="description",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="indicatoritems",
            name="in_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="indicators.indicators"
            ),
        ),
        migrations.AlterField(
            model_name="indicatoritems",
            name="min_effect",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="indicators",
            name="description",
            field=models.TextField(default=""),
        ),
    ]