from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage('media/files')


class Message(models.Model):

    id = models.AutoField(primary_key=True, unique=True, editable=False, blank=True)
    price = models.FloatField(default=5.0, blank=True, editable=False)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE)
    file = models.FileField(storage=fs, blank=True, null=True)
    text = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=20, blank=False)
    time = models.DateTimeField(blank=False)

    def __str__(self):
        return self.name



