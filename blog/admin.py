from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.template.defaultfilters import truncatechars, truncatewords

from blog.models import Author, Article


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = '__str__', 'bio',
    search_fields = 'user__username', 'bio',
    list_filter = 'user__is_active',


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = 'headline', 'snippet', 'author', 'time', 'published',
    list_editable = 'published',
    search_fields = 'headline', 'content',
    date_hierarchy = 'time'
    list_filter = 'published', 'author',

    def snippet(self, article):
        return truncatewords(article.content, 10)
