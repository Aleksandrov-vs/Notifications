from django.db import models
from users.models import User
# Create your models here.

# class CustomUser(User):
#     user = models.OneToOneField(verbose_name="реальный пользователь", to=User, on_delete=models.CASCADE,
#                                 related_name="customuser")
#     password1 = models.CharField(max_length=23)
#     password2 = models.CharField(max_length=23)
