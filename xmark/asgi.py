"""
ASGI config for xmark project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

# from xmark.routing import websocket_urlpatterns


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmark.settings.base")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.


django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
    }
)
