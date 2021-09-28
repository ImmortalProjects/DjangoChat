from django.db import models


class user(models.Model):
    user_name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
