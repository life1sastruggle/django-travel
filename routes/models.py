from django.db import models
from django.utils.timezone import now


class Routes(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    pic_url = models.URLField(blank=True)
    score = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    intro = models.TextField(blank=True)
    creation_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(blank=True)
    expiration_time = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'routes'
        verbose_name = 'route'
        verbose_name_plural = 'routes'

    def __str__(self):
        return self.name
