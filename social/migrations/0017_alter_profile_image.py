# Generated by Django 5.0.6 on 2024-05-28 22:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("social", "0016_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="https://res.cloudinary.com/ds1ozp6n5/image/upload/v1716935718/media/fm9buijf4zc4vr3xfu5p.jpg",
                upload_to="profile_img",
            ),
        ),
    ]
