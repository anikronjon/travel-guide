from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import gettext_lazy as _
from . import MediaVideo, MediaImage


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
    class DivisionChoices(models.TextChoices):
        BARISAL = 'BRS', _('Barisal')
        CHITTAGONG = 'CTG', _('Chittagong')
        DHAKA = 'DHK', _('Dhaka')
        Khulna = 'KLN', _('Khulna')
        MYMENSINGH = 'MMS', _('Mymensingh')
        RAJSHAHI = 'RJS', _('Rajshahi')
        RANGPUR = 'RGP', _('Rangpur')
        SYLHET = 'SYL', _('Sylhet')
    division = models.CharField(_('Division'), max_length=3, choices=DivisionChoices.choices)
    district = models.CharField(_('District'), max_length=20, unique=True)

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __str__(self):
        return "{} - {}".format(self.division, self.district)


# Place model
class TouristPlace(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='places', verbose_name=_('Category'))
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='places', verbose_name=_('Location'))
    name = models.CharField(_('Place'), max_length=100)
    slug = models.SlugField(_('Slug'), max_length=100)
    description = models.TextField(_('Description'))
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    label_image = models.ImageField(_('Label image'), upload_to='image/label/')
    image = GenericRelation(MediaImage)
    video = GenericRelation(MediaVideo)

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')

    def __str__(self):
        return self.name
