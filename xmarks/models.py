from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse

from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="parent_category",
        blank=True,
        null=True,
    )
    root = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("xmarks:category-detail", args=[str(self.id)])

    def __str__(self):
        return "%s" % self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

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
    is_favorite = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="bookmarks",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "bookmark"
        verbose_name_plural = "bookmarks"

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse("xmarks:bookmark-detail", args=[str(self.pk)])
