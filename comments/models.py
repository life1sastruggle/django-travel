from django.db import models
from django.utils.timezone import now


class Comments(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    body = models.TextField(blank=True)
    creation_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(blank=True)
    expiration_time = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.name
