__author__ = 'norad'

from django.contrib.gis.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()