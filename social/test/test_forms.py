from django.test import TestCase
from social.form import SignupForm, PostForm


class TestForms(TestCase):
    """
    Test Signup form and Postform
    """

    def test_signupform_valid(self):
        """
        test signupform with valid data
        """
        signup_form = SignupForm(data={
            'username': "test",
            'email': "test@example.com",
            'password1': "pass_test1234",
            'password2': "pass_test1234"
        })

        self.assertTrue(signup_form.is_valid())

    def test_signup_form_mismatch_passwords(self):
        """
        test error password don't match
        """
        signup_form = SignupForm(data={
            'username': "test",
            'email': "test@example.com",
            'password1': "pass_test",
            'password2': "pass_test1234"
        })

        self.assertFalse(signup_form.is_valid())
        self.assertEqual(signup_form.error_messages,
                         {'password_mismatch': 'The two password fields didn’t match.'})

    def test_signup_form_no_data(self):
        """
        test empty form
        """
        signup_form = SignupForm(data={})

        self.assertFalse(signup_form.is_valid())
        self.assertEqual(len(signup_form.errors), 4)

    def test_postform_valid(self):
        """
        test psotfrom with valid data
        """
        post_form = PostForm(data={
            'content': "test_content"
        })
        self.assertTrue(post_form.is_valid())
        self.assertEqual(post_form.cleaned_data['content'], "test_content")

    def test_postform_no_data(self):
        """
        test psotfrom with no data
        """
        post_form = PostForm(data={})

        self.assertFalse(post_form.is_valid())
