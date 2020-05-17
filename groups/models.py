from django.contrib.postgres.fields import ArrayField
from django.db import models
from .utils import createID


class Group(models.Model):

    id = models.CharField(primary_key=True, unique=True, max_length=10, default=createID, editable=False)
    manager = models.ForeignKey('users.User', related_name='user', on_delete=models.CASCADE)
    name = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name


class TelegramUser(models.Model):

    id = models.IntegerField(primary_key=True, null=False, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    nickname = models.CharField(max_length=50, null=False, blank=True)

    groups = ArrayField(
        ArrayField(
            models.CharField(max_length=10)
        ), null=True, blank=True
    )

    def __str__(self):
        return self.id

