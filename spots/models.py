from django.db import models
from django.utils.timezone import now


class Spots(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    picUrl = models.URLField(blank=True, null=True, db_column='pic_url')
    score = models.DecimalField(blank=True, max_digits=2, decimal_places=1, default=0.0)
    intro = models.TextField(blank=True, null=True)
    longitude = models.DecimalField(blank=True, null=True, decimal_places=7, max_digits=10)
    latitude = models.DecimalField(blank=True, null=True, decimal_places=7, max_digits=10)
    creationTime = models.DateTimeField(default=now, null=True, db_column='creation_time')
    updateTime = models.DateTimeField(blank=True, null=True, db_column='update_time')
    expirationTime = models.DateTimeField(blank=True, null=True, db_column='expiration_time')

    class Meta:
        ordering = ['creationTime', 'id']
        db_table = 'spots'
        verbose_name = 'Spot'
        verbose_name_plural = 'Spots'

    def __str__(self):
        return self.name
