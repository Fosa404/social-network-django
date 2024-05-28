from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.jpeg', upload_to='profile_img')

    def __str__(self) -> str:
        return f"{self.user.username} profile"

    def following(self):
        followed_users_ids = Follow.objects.filter(
            follower_user=self.user).values_list('followed_user_id', flat=True)

        return User.objects.filter(id__in=followed_users_ids)


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self) -> str:
        return f'{self.user.username}: {self.content}'


class Follow(models.Model):
    follower_user = models.ForeignKey(
        User, related_name='follower_users', on_delete=models.CASCADE)

    followed_user = models.ForeignKey(
        User, related_name='followed_users', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower_user} following {self.followed_user}'
