"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from . import keys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
for envvar in keys.envvars:
    os.environ.setdefault(envvar[0], envvar[1])

application = get_wsgi_application()
