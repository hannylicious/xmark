"""Forms for the xmarks app."""

from django import forms
from django.forms import ModelForm

from xmarks.models import Bookmark


class BookmarkForm(ModelForm):
    """Form for creating and updating Bookmarks."""

    class Meta:
        """Meta info for BookmarkForm."""

        model = Bookmark
        fields = [
            "created_by",
            "favorite",
            "frequent",
            "name",
            "url",
            "updated_by",
            "user",
        ]
        widgets = {
            "created_by": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "updated_by": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(BookmarkForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields["user"].initial = user
            self.initial["updated_by"] = user
            self.initial["created_by"] = user
