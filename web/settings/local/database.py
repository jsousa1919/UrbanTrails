__author__ = 'norad'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'urbantrails',
        'USER': 'justin',
        'PASSWORD': 'justin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}