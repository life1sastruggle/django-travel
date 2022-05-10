import random
import uuid

from django.db import models
from django.utils.timezone import now

from app.utils import generateUUID
from attraction.models import Attraction


class File(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default=generateUUID)
    creator_id = models.CharField(max_length=32, blank=True, null=True)
    deleter_id = models.CharField(max_length=32, blank=True, null=True)
    creation_time = models.DateTimeField(default=now, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class AttractionImage(File):
    attraction = models.ForeignKey(Attraction, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='attraction', verbose_name='image', null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'attraction_image'
        verbose_name = 'Attraction Image'
        verbose_name_plural = 'Attraction Images'

    def __str__(self):
        return self.name


class Banner(File):
    type = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='banner', verbose_name='image', null=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'banner'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.name
