from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='author')
    bio = models.TextField(null=True, blank=True, help_text='About the author')
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '{u.first_name} {u.last_name}'.format(u=self.user)

    class Meta:
        ordering = 'user__last_name', 'user__first_name',


class Article(models.Model):
    author = models.ForeignKey(Author, related_name='articles')
    published = models.BooleanField(default=True)
    time = models.DateTimeField(default=timezone.now)
    headline = models.CharField(max_length=100)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('article', args=[self.pk]) if self.published else reverse('article-list')

    def __str__(self):
        return self.headline

    class Meta:
        ordering = '-time',