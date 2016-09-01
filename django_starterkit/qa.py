try:
    from .common import *
except ImportError:
    pass

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'dbname',
       'USER': 'user',
       'PASSWORD': 'pass',
       'HOST': 'mysql',
       'PORT': '3306',
   },
}

STATIC_ROOT = "/usr/src/static/server"
ALLOWED_HOSTS = ["*", ]
