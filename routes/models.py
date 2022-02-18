from django.db import models
from django.utils.timezone import now


class Routes(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    picUrl = models.URLField(blank=True, null=True, db_column='pic_url')
    score = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, null=True)
    intro = models.TextField(blank=True, null=True)
    creationTime = models.DateTimeField(default=now, null=True, db_column='creation_time')
    updateTime = models.DateTimeField(blank=True, null=True, db_column='update_time')
    expirationTime = models.DateTimeField(blank=True, null=True, db_column='expiration_time')

    class Meta:
        ordering = ['creationTime', 'id']
        db_table = 'routes'
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return self.name


class RoutesSpotsRelation(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    routesId = models.CharField(max_length=32, blank=True, null=True, db_column='routes_id')
    spotsId = models.CharField(max_length=32, blank=True, null=True, db_column='spots_id')
    creationTime = models.DateTimeField(default=now, blank=True, null=True, db_column='creation_time')
    expirationTime = models.DateTimeField(blank=True, null=True, db_column='expiration_time')

    class Meta:
        ordering = ['creationTime', 'id']
        db_table = 'routes_spots_relation'
        verbose_name = 'RoutesSpotsRelation'
        verbose_name_plural = 'RoutesSpotsRelations'


