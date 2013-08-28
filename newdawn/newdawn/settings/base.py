"""Common settings and globals."""

from os.path import abspath, basename, dirname, join, normpath
from sys import path

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)

# See: https://docs.djangoproject.com/en/1.5/ref/settings/#std:setting-ALLOWED_HOSTS
ALLOWED_HOSTS = ['www.yoglam.com']

########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Kamol Mavlonov', 'kamoljan@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Asia/Singapore'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://static.yoglam.com/admin/'

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_ROOT = '/var/www/yoglam.com/'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
#STATIC_URL = '/static/'
STATIC_URL = 'http://static.yoglam.com/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = r"k8!wzy=9%$&e4q0rsmvev0yo!!22d1dq)ozd8!jq^omkfs3gh0"
########## END SECRET CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',

    # user -- An auth.User instance representing the currently logged-in user
    # (or an AnonymousUser instance, if the client isn't logged in).
    # messages -- A list of messages (as strings) that have been set
    # via the messages framework.
    # perms -- An instance of django.core.context_processors.PermWrapper,
    # representing the permissions that the currently logged-in user has.
    'django.contrib.auth.context_processors.auth',

    # https://github.com/omab/django-social-auth
    #'social_auth.context_processors.social_auth_by_name_backends',
    #'social_auth.context_processors.social_auth_backends',
    #'social_auth.context_processors.social_auth_login_redirect',
    'social_auth.context_processors.social_auth_by_type_backends',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    # 'django.contrib.admindocs',

)

AUTHENTICATION_BACKENDS = (
    #'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    #'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    #'social_auth.backends.google.GoogleBackend',
    #'social_auth.backends.yahoo.YahooBackend',
    #'social_auth.backends.contrib.linkedin.LinkedinBackend',
    #'social_auth.backends.contrib.LiveJournalBackend',
    #'social_auth.backends.contrib.orkut.OrkutBackend',
    #'social_auth.backends.contrib.orkut.FoursquareBackend',
    #'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',
    # https://github.com/krvss/django-social-auth
    'social_auth',
    # https://github.com/tomchristie/django-rest-framework
    'rest_framework',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'ad',
    'common',
    'search',
    'auth',
    'rest',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION

########## REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    #    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10,
}
########## END REST FRAMEWORK CONFIGURATION

########## DJANGO_SOCIAL_AUTH CONFIGURATION
# DJANGO_SOCIAL_AUTH API KEYS
FACEBOOK_APP_ID = '380944988688965'
FACEBOOK_API_SECRET = 'a62d83696f8cdc19b52d0747ea5de26e'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FOURSQUARE_CONSUMER_KEY = ''
FOURSQUARE_CONSUMER_SECRET = ''
GOOGLE_CONSUMER_KEY = ''
GOOGLE_CONSUMER_SECRET = ''
GOOGLE_OAUTH2_CLIENT_KEY = '938623095446.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'eKSfEtSeJPOaC0lDHzmcyLAm'
LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET = ''
ORKUT_CONSUMER_KEY = ''
ORKUT_CONSUMER_SECRET = ''
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# DJANGO_SOCIAL_AUTH URLs
LOGIN_URL = '/auth/login/'
# LOGIN_REDIRECT_URL = '/auth/logged/'
LOGIN_REDIRECT_URL = '/ad/new/'
LOGIN_ERROR_URL = '/auth/error/'

# Not mandatory, but recommended::
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

# Backends will store extra values from response by default, set this to False
# to avoid such behavior::
SOCIAL_AUTH_EXTRA_DATA = False

#- The update_user_details pipeline processor will set certain fields on user
#  objects, such as ``email``. Set this to a list of fields you only want to
#  set for newly created users:
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email', ]

# Session expiration time is an special value, it's recommended to define::
SOCIAL_AUTH_EXPIRATION = 'expires'

# TODO: setup in production
#  When your project is behind a reverse proxy that uses HTTPS the redirect URIs
#  can became with the wrong schema (``http://`` instead of ``https://``), and
#  might cause errors with the auth process, to force HTTPS in the final URIs
#  define this setting::
# SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# TODO: Fire memcached
#  The name of the last backend used to login is stored as a string in the
#  session under the key ``social_auth_last_login_backend``, the key can be
#  customized by defining this setting::
SOCIAL_AUTH_LAST_LOGIN = 'social_auth_last_login_backend'

# If you want to use the full email address as the username
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

##SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True
#SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'associate_complete'
#SOCIAL_AUTH_COMPLETE_URL_NAME  = 'complete'
#SOCIAL_AUTH_CREATE_USERS = False
#SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
#SOCIAL_AUTH_ERROR_KEY = 'social_errors'
##SOCIAL_AUTH_EXPIRATION = 'expires'
##SOCIAL_AUTH_RAISE_EXCEPTIONS = False


# To force CSRF protection define
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True

# If you want to revoke a provider's tokens on disconnect
SOCIAL_AUTH_REVOKE_TOKENS_ON_DISCONNECT = True

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'auth.pipeline.redirect_to_form',
    'auth.pipeline.username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
)
########## END DJANGO_SOCIAL_AUTH CONFIGURATION
