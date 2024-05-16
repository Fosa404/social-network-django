from django.test import TestCase, Client
from django.urls import reverse, resolve
from social.models import Profile, Post, Follow, User
import json
from datetime import datetime


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.post_url = reverse('post')

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

    def test_post_POST(self):
        user = User.objects.create(
            username="user_test",
            password="pass_test"
        )
        self.client.force_login(user)
        response = self.client.post(self.post_url, {'timestamp': datetime.now(),
                                                    'content': 'content2'})
        post = Post.objects.filter(content='content2').first()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(post.user_id, 1)
