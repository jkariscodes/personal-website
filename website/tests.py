from django.test import TestCase
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_landing_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_portfolio_page_status_code(self):
        response = self.client.get('/portfolio/')
        self.assertNotEqual(response.status_code, 400)

