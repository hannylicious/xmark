from django.contrib.auth import get_user_model
from django.test import TestCase
from xmarks.models import Category
from xmarks.forms import CategoryForm


class CategoryFormTestCase(TestCase):
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

    def test_valid_form_root_category(self):
        data = {"name": "TestCategory", "root": True, "category": None}
        form = CategoryForm(data)
        self.assertTrue(form.is_valid())

    def test_valid_form_non_root_category(self):
        data = {
            "name": "ChildCategory",
            "root": False,
            "category": self.category.id,
        }
        form = CategoryForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_both_root_and_parent_category(self):
        data = {
            "name": "InvalidCategory",
            "root": True,
            "category": self.category.id,
        }
        form = CategoryForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "If making a root Category, no parent Category can be chosen.",
            form.errors["__all__"],
        )

    def test_invalid_form_neither_root_nor_parent_category(self):
        data = {"name": "InvalidCategory", "root": False, "category": None}
        form = CategoryForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            "If making a non-root Category, a parent Category must be chosen.",
            form.errors["__all__"],
        )
