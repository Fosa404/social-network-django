# Generated by Django 5.0.6 on 2024-05-08 19:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("social", "0002_profile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="image",
        ),
    ]
