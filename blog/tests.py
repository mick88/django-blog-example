from __future__ import absolute_import, print_function, unicode_literals, division

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy

from blog.models import Author, Article


class ArticleListTest(TestCase):
    url = reverse_lazy('article-list')

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('testuser', email=None, password='password', first_name='Mark', last_name='Brown')
        cls.author = Author.objects.create(user=cls.user)

    def setUp(self):
        super(ArticleListTest, self).setUp()
        self.client.force_login(self.user)

    def test_article_list(self):
        Article.objects.create(
            author=self.author,
            headline='Test Article',
            content='Test Content',
            published=True,
        )
        response = self.client.get(self.url)
        self.assertContains(response, 'Test Article')
        self.assertContains(response, 'Mark Brown')
        self.assertNotContains(response, 'Test Content')
