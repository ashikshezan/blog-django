from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title to test on :)',
            author=self.user,
            content='Testing is so boring and hard do write :('
        )

    def test_post_content(self):
        self.assertEqual(self.post.title, 'A good title to test on :)')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(self.post.content,
                         'Testing is so boring and hard do write :(')

    def test_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Testing is so boring and hard do write :(')
        self.assertTemplateUsed(response, 'posts/home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/111111/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'posts/post_detail.html')
