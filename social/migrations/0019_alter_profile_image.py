# Generated by Django 5.0.6 on 2024-05-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("social", "0018_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(upload_to="profile_img"),
        ),
    ]
