__author__ = 'justin'

from django.contrib import admin
from trails.models import Trail, Venue, TrailVenue, GoogleReference

admin.site.register(GoogleReference)
admin.site.register(Trail)
admin.site.register(Venue)
admin.site.register(TrailVenue)