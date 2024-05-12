from django.test import SimpleTestCase
from django.urls import reverse, resolve
from social.views import feed, profile, signup, log_out, create_posts
from social.urls import LoginView


class TestUrls(SimpleTestCase):

    def test_feed_url_is_resolved(self):
        url = reverse('feed')
        self.assertEquals(resolve(url).func, feed)

    def test_profile_url_is_resolved(self):
        url = reverse('profile', args=['username'])
        self.assertEquals(resolve(url).func, profile)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, log_out)

    def test_create_posts_url_is_resolved(self):
        url = reverse('post')
        self.assertEquals(resolve(url).func, create_posts)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)
