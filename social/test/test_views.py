from django.test import TestCase, Client
from django.urls import reverse, resolve
from social.models import Profile, Post, Follow
import json


class TestViews(TestCase):

    def test_signup_view_GET(self):
        client = Client()
        response = client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'form/signup.html')

    def test_profile_view_GET(self):
        client = Client()
        response = client.get(reverse('profile', args=['username']))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response, '/login/?next=/profile/username/')

    def test_post_view_GET(self):
        client = Client()
        response = client.get(reverse('post'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response, '/login/?next=/post/')
