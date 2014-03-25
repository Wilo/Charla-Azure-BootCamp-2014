"""
Django settings for djangositeabc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+&a%g8kt7w2n$72!v-eo4p+ulvqpx!2%vtiw05f4qm#(1cim&m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
        'djangositeabc.apps.catalogo',    
)

THIRD_PARTY_APPS = (

)

INSTALLED_APPS = INSTALLED_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangositeabc.urls'

WSGI_APPLICATION = 'djangositeabc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'djangodb',
        'USER': 'azureuser@pl9c274iqq',
        'PASSWORD':'django123$',
        'HOST':'pl9c274iqq.database.windows.net',
        'PORT':'1433',
        'OPTIONS':{
               'driver':'SQL Server Native Client 11.0',
               'MARS_Connection':True,
        }
    }
 #   'default': {
 #       'ENGINE': 'django.db.backends.sqlite3',
 #       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #   }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\','/')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'djangositeabc/static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'djangositeabc/templates'),
)