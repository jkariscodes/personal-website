from django.utils import timezone
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
# from django.contrib.auth import get_user_model
# from .models import Post


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


# class BlogTests(TestCase):
#     """
#     Testing the blog posts.
#     """
#     pass
#
#
# class SignUpPageTests():
#     """
#     Test new user registration functionality.
#     """
#     pass

