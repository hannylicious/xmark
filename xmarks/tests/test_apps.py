from django.apps import apps
from django.test import TestCase
from xmarks.apps import XmarksConfig


class XmarksConfigTestCase(TestCase):
    def test_app_name(self):
        self.assertEqual(XmarksConfig.name, "xmarks")
        self.assertEqual(apps.get_app_config("xmarks").name, "xmarks")
