from django.db import models


class MessageBox(models.Model):
    message = models.CharField(max_length=100)
    
