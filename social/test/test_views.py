from django.test import TestCase, Client
from django.urls import reverse
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
        response = client.get(reverse('post'))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'social/post.html')
