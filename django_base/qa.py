try:
    from common import *
except ImportError:
    pass

DEBUG = True

TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecoaching',
        'USER': 'ecoaching_user',
        'PASSWORD': 'ecoaching#db@123',
        'HOST': 'localhost',
        'PORT': '',  # Set to empty string for default.
    },
    'api': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecm',
        'USER': 'postgres',
        'PASSWORD': 'ecoachingapi#123',
        'HOST': '45.55.225.195',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "main/static"),
)

STATIC_ROOT = "/tmp/ecoaching-statics"

COOKIE_DOMAIN = ".doroob-ecoaching.com"

CHAT_URL = "http://messaging.doroob.rocks"

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'http://d10ac25882244f9fa87d9466d460dd39:d4d237d76c9e4056be6b974bf84bd389@sitdev-sentry.cloudapp.net/7',
}

# Add raven to the list of installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    # ...
    'raven.contrib.django.raven_compat',
    'dev'
)
DEFAULT_EMPTY_IMAGE = "profile/default-user-image.png"
DEFAULT_EMPTY_COVER = ("covers/lop.png",
                       "covers/lop2.png")
ENABLE_SOCKETS = True
EMPLOYER_API_URL = "http://saudix.com:8003/"
DOROOB_URL = "http://saudix.com:8001/"
ECOACHING_URL = "http://saudix.com:8000/"