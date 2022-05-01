from django.db import models
from django.utils.timezone import now


class File(models.Model):
    id = models.CharField(max_length=32, primary_key=True, )
    url = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)
    source_id = models.CharField(max_length=32, blank=True, null=True)
    creator_id = models.CharField(max_length=32, blank=True, null=True)
    deleter_id = models.CharField(max_length=32, blank=True, null=True)
    creation_time = models.DateTimeField(default=now, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='media', verbose_name='image', null=True)

    class Meta:
        ordering = ['creation_time', 'id']
        db_table = 'file'
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return self.name
