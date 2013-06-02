__author__ = 'norad'

SECRET_KEY = '!^n)&amp;d21t=nb0xx-tp++orbx2$i-1kt5!mcdg9g&amp;&amp;qzdf%jo9-'
ALLOWED_HOSTS = []
SITE_ID = 1

ADMINS = (
    ('Justin Sousa', 'jsousa1919@gmail.com'),
)
MANAGERS = ADMINS

ROOT_URLCONF = 'urls'

AUTH_USER_MODEL = 'accounts.User'
SOCIAL_AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_auth.middleware.SocialAuthExceptionMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}
