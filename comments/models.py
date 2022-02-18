from django.db import models
from django.utils.timezone import now


class Comments(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    body = models.TextField(blank=True, null=True)
    creationTime = models.DateTimeField(default=now, db_column='creation_time')
    updateTime = models.DateTimeField(blank=True, null=True, db_column='update_time')
    expirationTime = models.DateTimeField(blank=True, null=True, db_column='expiration_time')

    class Meta:
        ordering = ['creationTime', 'id']
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
