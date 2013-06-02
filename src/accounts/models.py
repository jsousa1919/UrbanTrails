__author__ = 'justin'

from django.contrib.auth.models import AbstractUser as DjangoUser
from django.contrib.gis.db import models

from tags.models import Tag


class User(DjangoUser):
    favorite_tags = models.ManyToManyField(Tag, related_name='favorite_of', null=True, blank=True)

    @property
    def city(self):
        # TODO implement view social auth
        return "Jersey City"

    def __unicode__(self):
        return self.username

class Preferences(models.Model):
    user = models.OneToOneField(User, related_name='preferences')
    tutorial = models.BooleanField(default=True)
    location = models.PointField(null=True, blank=True)