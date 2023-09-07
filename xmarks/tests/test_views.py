import pytest
from django.test import TestCase
from django.urls import reverse

from users.models import User
from xmarks.models import Bookmark


class IndexViewTestCase(TestCase):
    def test_index_view(self):
        def call_index():
            self.client.get(reverse("xmarks:index"))

        user = User.objects.create_user(username="testuser", password="12345")
        bookmark = Bookmark.objects.create(
            name="test bookmark", url="https://www.google.com", user=user
        )
        bookmarks = Bookmark.objects.all()
        response = self.client.get(reverse("xmarks:index"))
        self.assertEqual(response.status_code, 302)
        self.assertNumQueries(0, call_index)
        self.assertContains(response, "Hello, world!")
