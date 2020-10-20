# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from .base import *

DEBUG = False

INSTALLED_APPS += [
    'mod_wsgi.server',
]

NUCLIO['HOST'] = os.getenv('CVAT_NUCLIO_HOST', 'nuclio')

for key in RQ_QUEUES:
    RQ_QUEUES[key]['HOST'] = os.getenv('CVAT_REDIS_HOST', 'cvat_redis')

CACHEOPS_REDIS['host'] = os.getenv('CVAT_REDIS_HOST', 'cvat_redis')

# Django-sendfile:
# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.xsendfile'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('CVAT_POSTGRES_HOST', 'cvat_db'),
        'NAME': os.getenv('CVAT_POSTGRES_DBNAME', 'postgres'),
        'USER': os.getenv('CVAT_POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('CVAT_POSTGRES_PASSWORD', 'vLaCAq8ZB4HEHWQvE228JTbpG296w8X8'),
    }
}

# dev only, need production ready settings
CORS_ALLOWED_ORIGINS = (
    'http://localhost:3000',
    'http://supa-cvat-ui.s3-ap-southeast-1.amazonaws.com',
    'https://supa-ui-exp.supahands.com',
)

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://supa-cvat-ui.s3-ap-southeast-1.amazonaws.com',
    'https://supa-ui-exp.supahands.com',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'X-CSRFToken',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://supa-cvat-ui.s3-ap-southeast-1.amazonaws.com',
    'https://supa-ui-exp.supahands.com',
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS= True
