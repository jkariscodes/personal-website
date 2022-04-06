from django.utils import timezone
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post


# TODO Create test cases for models
# class BlogTests(TestCase):
#     """
#     Test cases specific to the blog and blog posts.
#     """
#     def setUp(self) -> None:
#         self.user = get_user_model().objects.create_user(
#             username='jkariukidev',
#             email='contact@josephkariuki.com',
#             password='secret'
#         )
#         self.post = Post.objects.create(
#             title='Post the First',
#             body ='This the first post body.',
#             author=self.user,
#             published=timezone.now,
#             created=timezone.now,
#             updated=timezone.now,
#             category='Uncategorized',
#             status='default',
#         )
#
#     def test_get_absolute_url(self):
#         self.assertEqual(self.post.get_absolute_url(), 'blog/article/<slug:slug>/')
#
#     def test_post_content(self):
#         self.assertEqual(f'{self.post.title}', 'A good title')
#         self.assertEqual(f'{self.post.author}', 'testuser')
#         self.assertEqual(f'{self.post.body}', 'Nice body content')
#
#     def test_post_list_view(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Nice body content')
#         self.assertTemplateUsed(response, 'home.html')
#
#     def test_post_detail_view(self):
#         response = self.client.get('/post/1/')
#         no_response = self.client.get('/post/100000/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'A good title')
#         self.assertTemplateUsed(response, 'post_detail.html')
#
#     def test_post_create_view(self):
#         response = self.client.post(reverse('post_new'), {
#             'title': 'New title',
#             'body': 'New text',
#             'author': self.user.id,
#         })
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Post.objects.last().title, 'New title')
#         self.assertEqual(Post.objects.last().body, 'New text')


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

