from django.utils import timezone
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post


class WebsitePagesTests(SimpleTestCase):
    """
    Test page URL access.
    """
    def test_home_page_status_code(self):
        """
        Test home page return code status.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        """
        Test home page return code status.
        """
        response = self.client.get('/contact/')
        self.assertNotEqual(response.status_code, 400)

    def test_about_page_status_code(self):
        """
        Test home page return code status.
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_portfolio_page_status_code(self):
        """
        Test home page return code status.
        """
        response = self.client.get('/portfolio/')
        self.assertNotEqual(response.status_code, 500)


class SignUpPageTests(TestCase):
    """
    User registration tests.
    """
    username = 'new_user'
    email = 'me@josephkariuki.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/account/register/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('account:register'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('account:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_sign_up_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
