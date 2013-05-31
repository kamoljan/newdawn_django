"""Development settings and globals."""


from os.path import join, normpath

from base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newdawn',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'init_command': 'SET storage_engine=INNODB'}
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
########## END TOOLBAR CONFIGURATION

########## SUSHI CONFIGURATION
SUSHI_SECRET_KEY = '85d617c7e82c1ec51ee00bec5dca17e4'
SUSHI_URL = '127.0.0.1:8081'
SUSHI_PUBLIC_URL = 'http://sushi.colekaku.com/'
########## END SUSHI CONFIGURATION

########## SPHINX CONFIGURATION
SPHINX_SEARCHD_HOST = '127.0.0.1'
SPHINX_SEARCHD_PORT = '9312'
########## END SPHINX CONFIGURATION

########## DJANGO_SOCIAL_AUTH API KEYS ##########
FACEBOOK_APP_ID              = '380944988688965'
FACEBOOK_API_SECRET          = 'a62d83696f8cdc19b52d0747ea5de26e'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_KEY     = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''

########## DJANGO_SOCIAL_AUTH SETTINGS ##########
LOGIN_URL          = '/auth/login/'
LOGIN_REDIRECT_URL = '/auth/logged/'
LOGIN_ERROR_URL    = '/auth/error/'

##SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True
#SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'associate_complete'
#SOCIAL_AUTH_COMPLETE_URL_NAME  = 'complete'
#SOCIAL_AUTH_CREATE_USERS = False
#SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
#SOCIAL_AUTH_ERROR_KEY = 'social_errors'
##SOCIAL_AUTH_EXPIRATION = 'expires'
##SOCIAL_AUTH_RAISE_EXCEPTIONS = False
