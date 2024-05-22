"""
ASGI config for portfolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

settings_module = 'portfolio.deployment' if 'WEBSITE_NAME' in os.environ else 'portfolio.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
