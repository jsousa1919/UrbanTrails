__author__ = 'justin'

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
