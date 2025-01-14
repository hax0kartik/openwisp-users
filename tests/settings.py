import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'openwisp-users.db',
    }
}

SECRET_KEY = 'fn)t*+$)ugeyip6-#txyy$5wf2ervc0d2n#h)qb)y5@ly$t*@w'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'openwisp_utils.admin_theme',
    'django.contrib.admin',
    'django.contrib.sites',
    'django_extensions',
    'openwisp_users.accounts',  # only needed in test env
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'openwisp_users',
    'testapp'
]

AUTH_USER_MODEL = 'openwisp_users.User'
SITE_ID = '1'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TIME_ZONE = 'Europe/Rome'
LANGUAGE_CODE = 'en-gb'
USE_TZ = True
USE_I18N = False
USE_L10N = False
STATIC_URL = '/static/'
CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(BASE_DIR), 'openwisp_users', 'templates')
        ],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'openwisp_utils.admin_theme.context_processor.menu_items'
            ],
        },
    }
]

# during development only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGIN_REDIRECT_URL = 'admin:index'

OPENWISP_ORGANIZATON_USER_ADMIN = True
OPENWISP_ORGANIZATON_OWNER_ADMIN = True

# local settings must be imported before test runner otherwise they'll be ignored
try:
    from local_settings import *
except ImportError:
    pass
