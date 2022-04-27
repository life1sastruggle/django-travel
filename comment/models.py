from django.db import models
from django.utils.timezone import now

from attraction.models import Attraction


class Comment(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    text = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=2, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=32, blank=True, null=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, null=True)
    creation_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.attraction
