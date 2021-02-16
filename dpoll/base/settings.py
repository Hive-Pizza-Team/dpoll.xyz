import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#1bvvt+mgj=y4hi!j&bz_*%c4b&5u*01knw8(jzi58qaxe-19b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'sponsors',
    'communities',
    'rest_framework',
    'corsheaders',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares.LoginReferrerMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),

        ],        'APP_DIRS': True,
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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

AUTH_USER_MODEL = 'polls.User'


STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'static')

AUTHENTICATION_BACKENDS = [
    'polls.auth_backend.SteemConnectBackend',
    'django.contrib.auth.backends.ModelBackend',
]

from django.contrib import messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

COMMUNITY_TAG = "hive-120019"
DEFAULT_TAGS = ["hive-120019", "dpoll"]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

SESSION_COOKIE_AGE = 604800  # Default expire time of SC2 tokens

DPOLL_APP_VERSION = "0.0.2"

BENEFICIARY_ACCOUNTS = {
    "dpoll.sponsors": 1000,
}

CURATION_BOT_ACCOUNT = "dpoll.curation"
CURATION_BOT_POSTING_KEY = ""
PROMOTION_ACCOUNT = "dpoll.promotion"
PROMOTION_ACCOUNT_ACTIVE_KEY = ""
SPONSORS_ACCOUNT = "dpoll.sponsors"
DISCORD_CURATION_CHANNEL_ID = "508951346901286922"
BROADCAST_TO_BLOCKCHAIN = True

TEAM_MEMBERS = ["emrebeyler", "bluerobo", "isnochys", "tolgahanuzun"]


try:
    from .local_settings import *
except ImportError:
    pass

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

CORS_ORIGIN_ALLOW_ALL = True
