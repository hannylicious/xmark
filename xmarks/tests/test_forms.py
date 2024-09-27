"""Tests for the forms of the xmarks app."""
from django.contrib.auth import get_user_model
from django.test import TestCase

from xmarks.forms import BookmarkForm


class TestForms(TestCase):
    """Tests for the forms of the xmarks app."""

    def test_bookmark_form_valid_data_no_tags(self):
        """Test the BookmarkForm with valid data without tags."""
        user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        form = BookmarkForm(
            data={
                "name": "Test Bookmark",
                "url": "https://www.example.com",
                "favorite": True,
                "frequent": False,
                "tags_string": None,
                "user": user.id,
                "created_by": user.id,
                "updated_by": user.id,
            },
        )
        self.assertTrue(form.is_valid())

    def test_bookmark_form_valid_data_with_tags(self):
        """Test the BookmarkForm with valid data including tags."""
        user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        form = BookmarkForm(
            data={
                "name": "Test Bookmark",
                "url": "https://www.example.com",
                "favorite": True,
                "frequent": False,
                "tags_string": "test, example",
                "user": user.id,
                "created_by": user.id,
                "updated_by": user.id,
            }
        )
        self.assertTrue(form.is_valid())

    def test_bookmark_form_no_data(self):
        """Test the BookmarkForm with no data."""
        form = BookmarkForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)
        self.assertIn("name", form.errors.keys())
        self.assertIn("url", form.errors.keys())
        self.assertIn("user", form.errors.keys())
        self.assertIn("created_by", form.errors.keys())
        self.assertIn("updated_by", form.errors.keys())

    def test_bookmark_form_invalid_data(self):
        """Test the BookmarkForm with invalid data."""
        user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        form = BookmarkForm(
            data={
                "name": "Test Bookmark",
                "url": "not-a-url",
                "favorite": True,
                "frequent": False,
                "tags_string": "test, example",
                "user": user.id,
                "created_by": user.id,
                "updated_by": user.id,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(
            form.errors["url"], ["Enter a valid URL."]
        )