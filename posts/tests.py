from django.http import HttpRequest
from django.test import TestCase
from posts.models import Post
from posts.views import show_post_list, detail_post


class PostTest(TestCase):  # тест для главной страницы
    def test_list_post(self):
        request = HttpRequest()
        post = Post(title='Django')
        post.save()
        response = show_post_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django')

    def test_detail_post(self):  # тест перехода на страницу выбранного поста
        request = HttpRequest()
        post = Post(title='Save the World!')
        post.save()
        response = detail_post(request, post_id=post.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Save the World!')



