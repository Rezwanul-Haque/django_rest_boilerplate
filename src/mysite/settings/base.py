import os
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# API Version
API_VERSION = 'v1'

# Application definition
THIRD_PARTY_APPS = [
    'django_extensions',
    'rest_framework',
    'corsheaders',
]

CUSTOM_MANAGEMENT_APPS = [
    'core.apps.CoreConfig',
]

LOCAL_APPS = [
    # 'example.apps.ExamplesConfig',
    'api.apps.ApiConfig',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += THIRD_PARTY_APPS + CUSTOM_MANAGEMENT_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',  ## uncomment it for production use to use whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', ## corsheaders middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

# • AllowAny - any user, authenticated or not, has full access
# • IsAuthenticated - only authenticated, registered users have access
# • IsAdminUser - only admins/superusers have access
# • IsAuthenticatedOrReadOnly - unauthorized users can view any page, but only
#   authenticated users have write, edit, or delete privileges

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

## Session Related Settings

# SESSION_COOKIE_AGE = 1209600(Two Weeks)
# SESSION_COOKIE_DOMAIN = mydomain.com (enable cross-domain cookies) or None (standard domain cookie)
# SESSION_COOKIE_SECURE = True (HTTPS connection) or False (HTTP connection)
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True (session expire when browser closed) or False (session not expire when browser closed)
# SESSION_SAVE_EVERY_REQUEST = True (save the session to the database on every request and session expiration is also updated each time) or False 

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  ## STATICFILES_DIRS is the list of folders where Django will search for additional static files aside from the static folder of each app installed.
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root') ## STATIC_ROOT is the folder where static files will be stored after using manage.py collectstatic

# For Whitenoise
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  ## Uncomment it to use whitenoise in the production environment.
# Django built-In
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'  ## To test whether the problems are due to WhiteNoise or not, try swapping the WhiteNoise storage backend for the Django one

# Media Folder Settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  ## MEDIA_ROOT is the folder where files uploaded using FileField will go.

# Messages (Toaster message config)
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Email config
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS=True
