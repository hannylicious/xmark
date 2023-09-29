from django.test import TestCase
from channels.routing import ProtocolTypeRouter
from channels.layers import get_channel_layer

# Import the application object from asgi.py
from xmark.asgi import application, django_asgi_app


class ASGITestCase(TestCase):
    def test_asgi_application(self):
        # Ensure that the application object is an instance of ProtocolTypeRouter
        self.assertIsInstance(application, ProtocolTypeRouter)

        # Ensure that 'http' and 'websocket' protocols are defined
        self.assertIn("http", application.application_mapping)
        self.assertIn("websocket", application.application_mapping)

        # Ensure that the 'http' protocol points to the Django ASGI application
        self.assertEqual(
            application.application_mapping["http"], django_asgi_app
        )

    def test_channel_layer(self):
        # Ensure that a channel layer is correctly set up
        channel_layer = get_channel_layer()
        self.assertIsNotNone(channel_layer)
