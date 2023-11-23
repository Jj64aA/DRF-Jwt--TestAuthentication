from django.db import models
from django.contrib.models import user
# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()