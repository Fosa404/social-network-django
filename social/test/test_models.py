from django.test import TestCase
from social.models import Post, Follow, User
from datetime import datetime


class TestModels(TestCase):
    """
        Test models from social app
    """

    def setUp(self):
        """
            creating instances for the models
        """
        self.user = User.objects.create(
            username='user_test',
            password='pass_test'
        )
        self.user2 = User.objects.create(
            username='user2_test',
            password='pass2_test'
        )
        self.post = Post.objects.create(
            user=self.user,
            timestamp=datetime.now(),
            content='content_test'
        )
        self.follow = Follow.objects.create(
            follower_user=self.user,
            followed_user=self.user2
        )

    def test_user_following_user2(self):
        """
        test follow instance works
        """

        self.assertIn(self.user2,
                      self.user.profile.following())
