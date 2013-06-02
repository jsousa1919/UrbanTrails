__author__ = 'justin'

from django.contrib import admin
from accounts.models import User, Preferences

admin.site.register(User)
admin.site.register(Preferences)