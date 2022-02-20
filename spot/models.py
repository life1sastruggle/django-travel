from django.db import models
from django.utils.timezone import now


class Spot(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    pic_url = models.URLField(blank=True, null=True)
    score = models.DecimalField(blank=True, max_digits=2, decimal_places=1, default=0.0)
    intro = models.TextField(blank=True, null=True)
    longitude = models.DecimalField(blank=True, null=True, decimal_places=7, max_digits=10)
    latitude = models.DecimalField(blank=True, null=True, decimal_places=7, max_digits=10)
    creation_time = models.DateTimeField(default=now, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'spot'
        verbose_name = 'Spot'
        verbose_name_plural = 'Spots'

    def __str__(self):
        return self.name
