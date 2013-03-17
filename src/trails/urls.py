__author__ = 'norad'

from django.conf.urls import patterns, url
from trails.views import *

urlpatterns = patterns('trails.views',
                       url(r'^example/', example, name='example')
)
