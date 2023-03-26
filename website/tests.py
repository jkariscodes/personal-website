from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .models import Post
from .views import PortfolioPageView


class WebsitePagesTests(SimpleTestCase):
    """
    Test page URL access.
    """

    def test_home_page_status_code(self):
        """
        Test home page return code status.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        """
        Test home page return code status.
        """
        response = self.client.get("/contact/")
        self.assertNotEqual(response.status_code, 400)

    def test_about_page_status_code(self):
        """
        Test home page return code status.
        """
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_portfolio_page_status_code(self):
        """
        Test home page return code status.
        """
        response = self.client.get("/portfolio/")
        self.assertNotEqual(response.status_code, 500)

    def test_portfolio_url_resolves_homepageview(self):
        view = resolve("/portfolio/")
        self.assertEqual(view.func.__name__, PortfolioPageView.as_view().__name__)


class SignUpPageTests(TestCase):
    """
    User registration tests.
    """

    username = "new_user"
    email = "me@josephkariuki.com"

    def test_signup_page_status_code(self):
        response = self.client.get("/account/register/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("account:register"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("account:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

    def test_sign_up_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


class BlogTests(TestCase):
    """
    Test cases for blog and blog posts.
    """

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="new_user", email="me@josephkariuki.com", password="secret"
        )
        self.post = Post.objects.create(
            author=self.user,
            title="Post the First",
            body="Post the first",
            header_image="static/website/img/about.jpg",
        )

    def test_string_representation(self):
        post = Post(title="Some random Post", author=self.user)
        self.assertEqual(str(post), post.__str__())

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Post the First")
        self.assertEqual(f"{self.post.author}", "new_user")
        self.assertEqual(f"{self.post.body}", "Post the first")
        self.assertEqual(self.post.header_image, "static/website/img/about.jpg")

    def test_post_detail_view(self):
        response = self.client.get("/blog/article/post-the-first/")
        no_response = self.client.get("/blog/article/this-and-that/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Post the First")
        self.assertTemplateUsed(response, "article.html")

    def test_post_update_view(self):
        response = self.client.post(
            reverse("website:update_post", args="1"),
            {
                "title": "New Title",
                "body": "New text",
            },
        )
