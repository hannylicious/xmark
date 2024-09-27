"""Test URL patterns for xmarks app."""

from django.test import SimpleTestCase
from django.urls import resolve, reverse

from xmarks.views import (
    BookmarkCreateView,
    BookmarkDetailView,
    BookmarkListView,
    BookmarkUpdateView,
    IndexTemplateView,
    TagDetailView,
)


class TestUrlsResolve(SimpleTestCase):
    """Test URL patterns for xmarks app."""

    def test_index_url_resolves(self) -> None:
        """Test the index."""
        url = reverse("xmarks:index")
        self.assertEqual(resolve(url).func.view_class, IndexTemplateView)

    def test_tag_detail_url_resolves(self):
        url = reverse("xmarks:tag-detail", args=[1])  # /tags/1/
        self.assertEqual(resolve(url).func.view_class, TagDetailView)

    def test_bookmark_create_url_resolves(self):
        url = reverse("xmarks:bookmark-create")
        self.assertEqual(resolve(url).func.view_class, BookmarkCreateView)

    def test_bookmark_detail_url_resolves(self):
        url = reverse("xmarks:bookmark-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, BookmarkDetailView)

    def test_bookmark_update_url_resolves(self):
        url = reverse("xmarks:bookmark-update", args=[1])
        self.assertEqual(resolve(url).func.view_class, BookmarkUpdateView)

    def test_bookmark_list_url_resolves(self):
        url = reverse("xmarks:bookmark-list")
        self.assertEqual(resolve(url).func.view_class, BookmarkListView)

