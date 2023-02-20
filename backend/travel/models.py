from django.db import models
from django.utils.translation import gettext_lazy as _


# Category model
class Category(models.Model):
    name = models.CharField(_('Name'), max_length=50, unique=True)
    slug = models.SlugField(_('Slug'), max_length=50, unique=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


# Location Model
class Location(models.Model):
    division = models.CharField(_('Division'), max_length=20, unique=True)
    district = models.CharField(_('District'), max_length=20, unique=True)

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __str__(self):
        return "{} - {}".format(self.division, self.district)


# Place model
class Place(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='places', verbose_name=_('Category'))
    name = models.CharField(_('Place'), max_length=100)
    slug = models.SlugField(_('Slug'), max_length=100)
    description = models.TextField(_('Description'))
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')

    def __str__(self):
        return self.name


# Image upload path
def media_upload_path(instance, filename):
    return "{0}/{1}".format(instance.place.name, filename)


# Media model
class Media(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='medias', verbose_name=_('Place'))
    image = models.ImageField(_('Image'), upload_to=media_upload_path)


