"""
WSGI config for xmark project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import environ
from django.core.wsgi import get_wsgi_application

######
# Environment
######
ROOT_DIR = environ.Path(__file__) - 2
# Take environment variables from .env file
environ.Env.read_env(ROOT_DIR(".env"))

######
# Django Application
######
application = get_wsgi_application()
