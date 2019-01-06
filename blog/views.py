from __future__ import unicode_literals

from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from blog.models import Article


class PublicArticleMixin(object):
    """ Mixin class can be used in views to specify base queryset"""
    queryset = Article.objects.exclude(published=False)


class ArticleList(PublicArticleMixin, ListView):
    """ Page with the list of articles """
    template_name = 'blog/article_list.html'


class ArticleView(PublicArticleMixin, DetailView):
    """ Page with a single article """
    template_name = 'blog/article.html'
    pk_url_kwarg = 'pk'


class AuthorsOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return hasattr(self.request.user, 'author')

    @property
    def author(self):
        return self.request.user.author

class WriteArticleView(AuthorsOnlyMixin, CreateView):
    model = Article
    fields = 'headline', 'content',
    template_name = 'blog/article_form.html'

    def get_form_kwargs(self):
        kwargs = super(WriteArticleView, self).get_form_kwargs()
        kwargs['instance'] = Article(author=self.author, published=True)
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['author'] = self.author
        return super(WriteArticleView, self).get_context_data(**kwargs)
