from django.core.exceptions import ValidationError
from django.forms import ModelForm

from xmarks.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        root = cleaned_data["root"]
        category = cleaned_data["category"]
        if not root and not category:
            raise ValidationError(
                "If making a non-root Category, a parent Category must be chosen."
            )
        if root and category:
            raise ValidationError(
                "If making a root Category, no parent Category can be chosen."
            )
