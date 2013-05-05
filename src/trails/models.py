__author__ = 'norad'

from django.contrib.gis.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()


class GoogleReference(models.Model):
    reference_id = models.CharField(max_length=64)


class Venue(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.PointField()
    reference = models.ForeignKey(GoogleReference, null=True, blank=True)
    tags = models.ManyToManyField(Tag)


class Trail(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)


class TrailVenue(models.Model):
    trail = models.ForeignKey(Trail)
    venue = models.ForeignKey(Venue)
    order = models.IntegerField()