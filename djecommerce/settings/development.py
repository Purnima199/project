from .base import *
from decouple import config

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# STRIPE_PUBLIC_KEY = config('pk_test_51NhZ1AI9MTeJtH1HNQ1PrdjGuRLKJeajf5dpxTcWdLqC80sMeCOjJXbYk5CPOhJzoE9W4Qy5Eev7L5Yo1WIT9Y6400xAR5jH0m')
# STRIPE_SECRET_KEY = config('sk_test_51NhZ1AI9MTeJtH1Hk4HwW8824O6D6Pk1R6y7S7s9mluVRDp5Cl4XwMnqB8voKemrmh3CIgWHzIc8PcmoGvvxajYG00IIyiwixU')
STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default='')

STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default='')
