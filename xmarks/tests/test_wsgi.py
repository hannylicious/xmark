from django.test import TestCase
from django.core.handlers.wsgi import WSGIHandler

# Import the application object from wsgi.py
from xmark.wsgi import application


class WSGITestCase(TestCase):
    def test_wsgi_application(self):
        # Ensure that the application object is an instance of WSGIHandler
        self.assertIsInstance(application, WSGIHandler)
