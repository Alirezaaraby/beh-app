# Generated by Django 4.2.13 on 2024-06-06 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_permissions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permissions",
            name="pid",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                unique=True,
            ),
        ),
    ]
