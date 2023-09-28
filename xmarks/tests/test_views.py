import pytest
from django.test import TestCase
from django.urls import reverse

from users.models import User
from xmarks.models import Bookmark


class ViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="testuser", password="12345")

    def call_index(self):
        self.client.get(reverse("xmarks:index"))


class IndexViewTestCase(ViewTestCase):
    def test_index_view_redirects_non_authenticated_users(self):
        response = self.client.get(reverse("xmarks:index"))
        self.assertEqual(response.status_code, 302)
        self.assertNumQueries(0, self.call_index)
        self.assertEqual(response.url, reverse("login") + "?next=/xmarks/")

    def test_index_view_loads_for_authenticated_users(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("xmarks:index"))
        self.assertEqual(response.status_code, 200)
        self.assertNumQueries(3, self.call_index)
        self.assertTemplateUsed(response, "xmarks/index.html")
