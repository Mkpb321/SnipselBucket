import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# Settings on windows machine (development)

if os.name == 'nt':
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    STATIC_ROOT = ''


# Settings on linux server (deployment)

if os.name == 'posix':
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    STATIC_ROOT = '/home/SnipselBucket/SnipselBucket/snipselbucketsite/static'
    # SECURE_SSL_REDIRECT = True
    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True