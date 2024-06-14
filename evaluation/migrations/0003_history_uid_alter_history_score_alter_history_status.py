# Generated by Django 4.2.13 on 2024-06-13 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0005_alter_assessments_overhead_level"),
        ("evaluation", "0002_alter_history_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="history",
            name="uid",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dashboard.assessments",
            ),
        ),
        migrations.AlterField(
            model_name="history",
            name="score",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="history",
            name="status",
            field=models.CharField(max_length=250),
        ),
    ]
