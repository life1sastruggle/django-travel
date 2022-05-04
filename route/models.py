import random
import uuid

from django.db import models
from django.utils.timezone import now

from attraction.models import Attraction


class Route(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default=''.join(str((uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid1()) + str(random.random())))).split('-')))
    name = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='route', verbose_name='image', null=True)
    score = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, null=True)
    introduction = models.TextField(blank=True, null=True)
    attraction = models.ManyToManyField(Attraction, through='RouteAttractionMapping')
    creation_time = models.DateTimeField(default=now, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'route'
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return self.name


class RouteAttractionMapping(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(default=now, blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'route_attraction_mapping'
        verbose_name = 'RouteAttractionMapping'
        verbose_name_plural = 'RouteAttractionMappings'
