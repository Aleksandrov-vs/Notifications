from django.db import models


class TextMessageModel(models.Model):

    group = models.ForeignKey('groups.Group', related_name='group', on_delete=models.CASCADE)
    price = models.FloatField(default=5.0, editable=False, blank=True)
    text = models.CharField(max_length=255)