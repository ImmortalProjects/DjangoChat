from django.db import models
from django.contrib.auth.models import User


class MessageBox(models.Model):
    message = models.CharField(max_length=100)
    room_name = models.CharField(max_length=100, default=None)
