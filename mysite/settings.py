"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
''' moved to dev.py
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sgsdzy_a7mf&$n7!qk8v4-ohl5&&2o^83t!t+2+cwq&e73p!r$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
'''
'''
DEBUG = False

ALLOWED_HOSTS = ['*']
'''


# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'blog',
    'django.contrib.humanize',
    'django_extensions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    "debug_toolbar", 
    'taggit',
    'django_summernote',
    'captcha',
    'accounts',
]
''' move to dev
# site's frameworks
SITE_ID = 2
'''
# robots
ROBOTS_USE_HOST = True
ROBOTS_USE_SITEMAP = True

# summernote's configs
SUMMERNOTE_THEME = 'bs4'

# captcha admin setting
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
    # 'engine': 'recaptcha',
    # 'engine': 'recaptcha2',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

'''move to dev
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
'''move to dev
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
'''
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1",
]
'''move to dev
X_FRAME_OPTIONS = 'SAMEORIGIN'
'''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nik.django.2004@gmail.com'
# EMAIL_HOST_PASSWORD = 'django12345678'
EMAIL_HOST_PASSWORD = 'pfjt xwus pjmo kfua'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
'''move to prod
CSRF_COOKIE_SECURE = True
'''
