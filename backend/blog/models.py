from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Published Manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', _('Draft')
        PUBLISHED = 'PB', _('Published')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name=_('Author'))
    title = models.CharField(_('Title'), max_length=250)
    slug = models.SlugField(_('Slug'), max_length=250, unique_for_date='created')
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    status = models.CharField(_('Status'), max_length=2, choices=Status.choices, default=Status.DRAFT)
    body = models.TextField(_('Body'))
    # manager
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        created = timezone.make_naive(self.created)
        return reverse('blog:post_detail', args=[created.year, created.month, created.day, self.slug])
