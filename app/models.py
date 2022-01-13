from enum import auto
from django.db import models

# Create your models here.
class TempFile(models.Model):
    file = models.FileField(upload_to="temp", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def file_path(self): return self.file.storage.url


class Data(models.Model):
    state = models.CharField(max_length=256)
    other = models.CharField(max_length=256)