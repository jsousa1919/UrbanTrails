__author__ = 'norad'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'urbantrails',
        'USER': 'postgres',
        'PASSWORD': 'Urb@nTr@ils',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}