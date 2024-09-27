"""Tests for the views of the xmarks app."""

import pytest
from django.test import TestCase, Client
from django.urls import reverse

from users.models import User
from xmarks.models import Bookmark, Tag


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="test_user", password="password"
        )
        self.client.login(username="test_user", password="password")

    def call_index(self):
        self.client.get(reverse("xmarks:index"))


class IndexViewTestCase(ViewTestCase):
    def test_index_view_redirects_non_authenticated_users(self):
        self.client.logout()
        response = self.client.get(reverse("xmarks:index"))
        self.assertEqual(response.status_code, 302)
        self.assertNumQueries(0, self.call_index)
        self.assertEqual(response.url, reverse("login") + "?next=/xmarks/")

    def test_view_is_accessible_to_logged_in_users(self):
        response = self.client.get(reverse("xmarks:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse("xmarks:index"))
        self.assertTemplateUsed(response, "xmarks/index.html")

    def test_view_passes_correct_context_data(self):
        bookmark = Bookmark.objects.create(
            user=self.user,
            name="Test Bookmark",
            created_by=self.user,
            updated_by=self.user,
        )

        response = self.client.get(reverse("xmarks:index"))

        self.assertIn("bookmarks", response.context)
        self.assertEqual(list(response.context["bookmarks"]), [bookmark])

        self.assertIn("favorite_bookmarks", response.context)
        self.assertEqual(list(response.context["favorite_bookmarks"]), [])


class TagDetailViewTests(ViewTestCase):
    def setUp(self):
        super().setUp()
        self.tag = Tag.objects.create(
            name="Test Tag",
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_view_is_accessible_to_logged_in_users(self):
        response = self.client.get(
            reverse("xmarks:tag-detail", kwargs={"pk": self.tag.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_is_not_accessible_to_anonymous_users(self):
        self.client.logout()
        response = self.client.get(
            reverse("xmarks:tag-detail", kwargs={"pk": self.tag.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, reverse("login") + "?next=/xmarks/tags/1/"
        )

    def test_view_renders_correct_template(self):
        response = self.client.get(
            reverse("xmarks:tag-detail", kwargs={"pk": self.tag.pk})
        )
        self.assertTemplateUsed(response, "xmarks/tag_detail.html")

    def test_view_passes_correct_context_data(self):
        response = self.client.get(
            reverse("xmarks:tag-detail", kwargs={"pk": self.tag.pk})
        )

        self.assertIn("tag", response.context)
        self.assertEqual(response.context["tag"], self.tag)


class BookmarkDetailViewTests(ViewTestCase):
    def setUp(self):
        super().setUp()
        self.bookmark = Bookmark.objects.create(
            name="Test Bookmark",
            url="https://example.com",
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(
            reverse("xmarks:bookmark-detail", kwargs={"pk": self.bookmark.pk})
        )
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_view_bookmark(self):
        self.client.login(username="test_user", password="password")
        response = self.client.get(
            reverse("xmarks:bookmark-detail", kwargs={"pk": self.bookmark.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_context_data_contains_bookmark(self):
        self.client.login(username="test_user", password="password")
        response = self.client.get(
            reverse("xmarks:bookmark-detail", kwargs={"pk": self.bookmark.pk})
        )
        context = response.context
        self.assertIn("bookmark", context)
        self.assertEqual(context["bookmark"], self.bookmark)


class BookmarkCreateViewTests(ViewTestCase):
    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("xmarks:bookmark-create"))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_create_bookmark(self):
        response = self.client.post(
            reverse("xmarks:bookmark-create"),
            data={
                "name": "Test Bookmark",
                "url": "https://example.com",
            },
        )
        self.assertEqual(response.status_code, 302)
        bookmark = Bookmark.objects.get(name="Test Bookmark")
        self.assertEqual(bookmark.user, self.user)
        self.assertEqual(bookmark.created_by, self.user)
        self.assertEqual(bookmark.updated_by, self.user)

    def test_invalid_form_data_re_renders_form(self):
        response = self.client.post(
            reverse("xmarks:bookmark-create"),
            data={
                "name": "",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)


class BookmarkUpdateViewTests(ViewTestCase):
    def setUp(self):
        super().setUp()
        self.bookmark = Bookmark.objects.create(
            name="Test Bookmark",
            url="https://example.com",
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(
            reverse("xmarks:bookmark-update", kwargs={"pk": self.bookmark.pk})
        )
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_update_bookmark(self):
        response = self.client.post(
            reverse("xmarks:bookmark-update", kwargs={"pk": self.bookmark.pk}),
            data={
                "name": "Updated Test Bookmark",
                "url": "https://example.com",
            },
        )
        self.assertEqual(response.status_code, 302)
        bookmark = Bookmark.objects.get(pk=self.bookmark.pk)
        self.assertEqual(bookmark.name, "Updated Test Bookmark")
        self.assertEqual(bookmark.updated_by, self.user)

    def test_invalid_form_data_re_renders_form(self):
        response = self.client.post(
            reverse("xmarks:bookmark-update", kwargs={"pk": self.bookmark.pk}),
            data={
                "name": "",
                "url": "https://example.com",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)


class BookmarkListViewTests(ViewTestCase):
    def setUp(self):
        super().setUp()
        self.bookmarks = [
            Bookmark.objects.create(
                name="Bookmark 1",
                url="https://example.com",
                user=self.user,
                created_by=self.user,
                updated_by=self.user,
            ),
            Bookmark.objects.create(
                name="Bookmark 2",
                url="https://example.com",
                user=self.user,
                created_by=self.user,
                updated_by=self.user,
            ),
        ]

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("xmarks:bookmark-list"))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_see_list_of_bookmarks(self):
        response = self.client.get(reverse("xmarks:bookmark-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["bookmarks"]), 2)

    def test_bookmarks_are_ordered_by_category(self):
        response = self.client.get(reverse("xmarks:bookmark-list"))
        bookmarks = response.context["bookmarks"]
        self.assertEqual(bookmarks[0].name, "Bookmark 1")
        self.assertEqual(bookmarks[1].name, "Bookmark 2")

    def test_context_data_contains_bookmarks(self):
        response = self.client.get(reverse("xmarks:bookmark-list"))
        context = response.context
        self.assertIn("bookmarks", context)
        self.assertEqual(list(context["bookmarks"]), self.bookmarks)


