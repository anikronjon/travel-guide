from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Image upload path
def media_upload_path(instance, filename):
    return "{0}/{1}".format(instance.place.name, filename)


def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # 5 MB
    if image.size > max_size:
        raise ValidationError(f'The image size ({image.size} bytes) exceeds the maximum allowed size of {max_size} bytes.')


def validate_video_size(video):
    max_size = 20 * 1024 * 1024  # 20 MB
    if video.size > max_size:
        raise ValidationError(f'The image size ({video.size} bytes) exceeds the maximum allowed size of {max_size} bytes.')


# MediaVideo model
class MediaImage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(content_type, object_id)
    image = models.ImageField(_('Image'), upload_to=media_upload_path, validators=[validate_image_size])


# MediaVideo model
class MediaVideo(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(content_type, object_id)
    video = models.ImageField(_('Video'), upload_to=media_upload_path, validators=[validate_video_size])
