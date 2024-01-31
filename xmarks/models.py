from django.conf import settings
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_created_by",
        on_delete=models.PROTECT,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_updated_by",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse("xmarks:tag-detail", args=[str(self.id)])


# Bookmark model
class Bookmark(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    favorite = models.BooleanField(default=False)
    frequent = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_created_by",
        on_delete=models.PROTECT,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_updated_by",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = "bookmark"
        verbose_name_plural = "bookmarks"

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse("xmarks:bookmark-detail", args=[str(self.pk)])


# TODO: considerations for tags / misspellings of / recommendations for
