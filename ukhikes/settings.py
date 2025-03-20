"""
This file contains the configuration for the UK Hikes project. It sets up
the base directory, security settings, installed applications, middleware,
database configuration, static and media file handling, and third-party
services (such as Cloudinary).
"""

from pathlib import Path
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-secret-key')
DEBUG = False

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_REDIRECT_URL = '/profile/'

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".herokuapp.com",
    "ukhikes-blog.herokuapp.com",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1",
    "http://localhost",
    "https://ukhikes-blog.herokuapp.com",
    "https://*.herokuapp.com",
]

# === Security & SSL Settings ===
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS
SESSION_COOKIE_SECURE = True  # Secure session cookies
CSRF_COOKIE_SECURE = True  # Secure CSRF cookies

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year (Recommended for security)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True  # Preload HSTS (for better browser enforcement)

# Prevent security vulnerabilities
SECURE_BROWSER_XSS_FILTER = True  # Protect against XSS attacks
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME-based attacks

# Trust Heroku's SSL forwarding
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'crispy_bootstrap5',
    'blog',
    'profiles',
    'testimonials',
    'cloudinary_storage',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'ukhikes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'profiles', 'templates'),
            os.path.join(BASE_DIR, 'blog', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'ukhikes.wsgi.application'

# === Database Configuration ===
# Only use dj_database_url if DATABASE_URL is provided and non-empty.
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.'
             'UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.'
             'MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.'
             'CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.'
             'NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = ''

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME', 'dgv1yketq'),
    api_key=os.getenv('CLOUDINARY_API_KEY', '759353575921226'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET', 'F6Xb3lMjRQODJ_eXK2du4-tQmWw')
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Allauth Configuration
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_FORMS = {"signup": "profiles.forms.CustomSignupForm"}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Automatically configure settings for Heroku (including logging & database)
django_heroku.settings(locals())
