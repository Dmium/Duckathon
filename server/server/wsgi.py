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
os.environ.setdefault('SPOTIPY_CLIENT_ID', keys.SPOTIPY_CLIENT_ID)
os.environ.setdefault('SPOTIPY_CLIENT_SECRET', keys.SPOTIPY_CLIENT_SECRET)
os.environ.setdefault('SPOTIPY_REDIRECT_URI', keys.SPOTIPY_REDIRECT_URI)

application = get_wsgi_application()
