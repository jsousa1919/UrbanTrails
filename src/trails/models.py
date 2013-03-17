__author__ = 'norad'

from django.contrib.gis.db import models

from tags.models import Tag


class GoogleReference(models.Model):
    reference_id = models.CharField(max_length=64)


class Venue(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.PointField()
    reference = models.ForeignKey(GoogleReference, null=True, blank=True)


class Trail(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()


class TrailVenue(models.Model):
    trail = models.ForeignKey(Trail)
    venue = models.ForeignKey(Venue)
    order = models.IntegerField()