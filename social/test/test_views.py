from django.test import TestCase, Client
from django.urls import reverse
from social.models import Profile, Post, Follow, User
import json
from datetime import datetime


class TestViews(TestCase):
    """
        Test views from social
    """

    def setUp(self):
        """
            set up the client test and post's and feed's urls 
        """

        self.client = Client()
        self.post_url = reverse('post')
        self.feed_url = reverse('feed')

    def test_feed_view_POST(self):
        """
            test POST method for feed view, wich search for a
            username and redirect to the profile view for that user
        """
        user = User.objects.create(
            username="user_test",   # user for login
            password="pass_test"
        )
        user2 = User.objects.create(
            username="user2_test",  # user to search
            password="pass2_test"
        )

        self.client.force_login(user)
        response = self.client.post(self.feed_url, {'search_users': 'user2'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/user2_test/')

    def test_signup_view_GET(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'form/signup.html')

    def test_profile_view_GET(self):
        response = self.client.get(reverse('profile', args=['username']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response, '/login/?next=/profile/username/')

    def test_post_view_GET(self):
        response = self.client.get(self.post_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response, '/login/?next=/post/')

    def test_post_view_POST(self):
        user = User.objects.create(
            username="user_test",
            password="pass_test"
        )
        self.client.force_login(user)
        response = self.client.post(self.post_url, {'timestamp': datetime.now(),
                                                    'content': 'content2'})
        post = Post.objects.filter(content='content2').first()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(post.user_id, 7)
