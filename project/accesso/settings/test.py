from __future__ import absolute_import

from .base import *

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": env.db('sqlite://:memory:'),
}


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
########## END EMAIL CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#     'default': env.cache_url_config('locmem://'),
# }
########## END CACHE CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING['loggers']['django.request'] = {
    'handlers': ['console', ],
    'level': 'DEBUG',
    'propagate': True
}
LOGGING['loggers']['accesso'] = {
    'handlers': ['console', ],
    'level': 'DEBUG',
    'propagate': True
}
########## END LOGGING CONFIGURATION