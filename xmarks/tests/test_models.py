from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from xmarks.models import Bookmark, Tag


class TagModelTestCase(TestCase):
    def setUp(self):        # RUNS BEFORE EACH TEST
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.tag = Tag.objects.create(
            name="ATag",
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_tag_creation(self):
        tag = Tag.objects.create(
            name="TestTag",
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )
        self.assertIsInstance(tag, Tag)
        self.assertEqual(tag.name, "TestTag")
        self.assertEqual(str(tag), "TestTag")

    def test_get_absolute_url(self):
        # Generate the expected URL
        expected_url = reverse("xmarks:tag-detail", args=[str(self.tag.pk)])

        # Assert that the method returns the expected URL
        self.assertEqual(self.tag.get_absolute_url(), expected_url)


class BookmarkModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.category = Category.objects.create(
            name="ParentCategory",
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )
        self.tag1 = Tag.objects.create(
            name="Tag1",
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )
        self.tag2 = Tag.objects.create(
            name="Tag2",
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )
        self.bookmark = Bookmark.objects.create(
            name="ABookmark",
            url="https://www.example.com",
            category=self.category,
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_bookmark_creation(self):
        bookmark = Bookmark.objects.create(
            name="TestBookmark",
            url="https://www.example.com",
            category=self.category,
            user=self.user,
            created_by=self.user,
            updated_by=self.user,
        )
        bookmark.tags.add(self.tag1, self.tag2)

        self.assertIsInstance(bookmark, Bookmark)
        self.assertEqual(bookmark.name, "TestBookmark")
        self.assertIn(self.tag1, bookmark.tags.all())
        self.assertIn(self.tag2, bookmark.tags.all())
        self.assertEqual(str(bookmark), "TestBookmark")

    def test_get_absolute_url(self):
        # Generate the expected URL
        expected_url = reverse(
            "xmarks:bookmark-detail", args=[str(self.bookmark.pk)]
        )

        # Assert that the method returns the expected URL
        self.assertEqual(self.bookmark.get_absolute_url(), expected_url)
