"""
Django settings for crumpa project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tdlh(_pt^h^)g8hzq!7%xtq7j16-h(=ctr)%6uv^xv=5--abb3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Note that the default IP address, 127.0.0.1,
# is not accessible from other machines on your network.
# To make your development server viewable to other machines on the network,
# use its own IP address (e.g. 192.168.0.101) or 0.0.0.0 or :: (with IPv6 enabled).
# Thus if run with "$ python manage.py runserver 0.0.0.0:8000" it will be available
# on all machinces in the local network, not just on the local 127.0.0.1
# (like if just run with "$ python manage.py runserver 8000")
# If run with specified ID/HOST then it has to be added in the ALLOWED_HOSTS array
ALLOWED_HOSTS = ["127.0.0.1", "192.168.0.101", "crampa.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # added some crispy forms
    'crispy_forms',
    
    'views',
    'profiles',

    # Needed for Django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crumpa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [ 
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crumpa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# By default, the development server doesn’t serve any static files for your site
# (such as CSS files, images, things under MEDIA_URL and so forth).
# It has to be configured explicitely if wanted "$ python manage.py runserver" to server them
# !!! THIS SHOULD BE DONE ONLY IN DEVELOPMENT MODE, NOT PRODUCTION
if DEBUG:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'media')
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'static-only')
    STATICFILES_DIRS = [os.path.join(os.path.dirname(BASE_DIR), 'static', 'static')]

# Template framework for CrispyForms - bootsrap (default), bootstrap3,
# bootstrap4, foundation, uni-form
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Needed for Django-allauth

SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_URL_PREFIX = "account"
LOGIN_URL = "/" + ACCOUNT_URL_PREFIX + "/login/"
LOGIN_REDIRECT_URL = "/"
from .settings_allauth import *

# Email sending settings
from .settings_email import *