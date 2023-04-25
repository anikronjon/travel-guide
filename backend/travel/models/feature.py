from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import gettext_lazy as _


class FeatureBaseModel(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    slug = models.SlugField(_('Slug'), max_length=120, unique=True)
    short_description = models.CharField(max_length=250)
    long_description = models.TextField()
    website = models.URLField(max_length=120)
    label_image = models.ImageField(upload_to='image/label')
    image = GenericRelation('MediaImage')
    video = GenericRelation('MediaVideo')

    class Meta:
        abstract = True


class Hotel(FeatureBaseModel):
    pass


class Restaurant(FeatureBaseModel):
    pass


class Agency(FeatureBaseModel):
    pass

