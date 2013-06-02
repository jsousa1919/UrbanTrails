__author__ = 'justin'

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from tags.models import Tag

