# Generated by Django 5.0.6 on 2024-05-28 22:37

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("social", "0015_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=cloudinary.models.CloudinaryField(
                default="https://res.cloudinary.com/ds1ozp6n5/image/upload/v1716935718/media/fm9buijf4zc4vr3xfu5p.jpg",
                max_length=255,
            ),
        ),
    ]
