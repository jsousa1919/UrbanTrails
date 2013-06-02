__author__ = 'norad'

from django.contrib.gis.db import models
from django.db.models import Q
from django.utils.functional import cached_property

from accounts.models import User
from tags.models import Tag


class GoogleReference(models.Model):
    reference_id = models.CharField(max_length=64)


class Venue(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.PointField()
    reference = models.ForeignKey(GoogleReference, null=True, blank=True, related_name="venues")
    tags = models.ManyToManyField(Tag, related_name="venues_tagged", null=True, blank=True)


class Trail(models.Model):
    name = models.CharField(max_length=64, default="My Urban Trail")
    description = models.TextField(default="This is my new trail!")
    creator = models.ForeignKey(User, related_name="trails_created")
    editors = models.ManyToManyField(User, related_name="trails_permitted", null=True, blank=True)
    map_id = models.CharField(max_length=64, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="trails_tagged", null=True, blank=True)

    def edit_permitted(self, user):
        return self.creator == user or self.editors.filter(pk=user.pk).exists()


class TrailVenue(models.Model):
    trail = models.ForeignKey(Trail)
    venue = models.ForeignKey(Venue)
    order = models.IntegerField()