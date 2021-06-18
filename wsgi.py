"""
WSGI config for locallibrary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")

from django.core.wsgi import get_wsgi_application

# from whitenoise.django import DjangoWhiteNoise
# http://whitenoise.evans.io/en/stable/changelog.html#v4-0

application = get_wsgi_application()

# application = DjangoWhiteNoise(application)
