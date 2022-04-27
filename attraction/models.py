from django.db import models
from django.utils.timezone import now


class Attraction(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.TextField(blank=True, null=True)
    scenery_score = models.DecimalField(blank=True, null=True, decimal_places=9, max_digits=10)
    repast_score = models.DecimalField(blank=True, null=True, decimal_places=9, max_digits=10)
    accommodation_score = models.DecimalField(blank=True, null=True, decimal_places=9, max_digits=10)
    shopping_score = models.DecimalField(blank=True, null=True, decimal_places=9, max_digits=10)
    entertainment_score = models.DecimalField(blank=True, null=True, decimal_places=9, max_digits=10)
    traffic_score = models.DecimalField(blank=True, null=True, decimal_places=9, max_digits=10)
    other_score = models.DecimalField(blank=True, null=True, decimal_places=9, max_digits=10)
    intro = models.TextField(blank=True, null=True)
    creation_time = models.DateTimeField(default=now, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'attraction'
        verbose_name = 'attraction'
        verbose_name_plural = 'Attractions'

    def __str__(self):
        return self.name
