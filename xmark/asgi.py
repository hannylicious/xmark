"""
ASGI config for xmark project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
from django.core.asgi import get_asgi_application

from xmark import urls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmark.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # Additional protocols go here:
        "websocket": OriginValidator(
            AuthMiddlewareStack(URLRouter(urls.websocket_urlpatterns)),
            ["*"],  # Allow any origin
        ),
    }
)
