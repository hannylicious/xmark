from django.urls import path

from . import views

app_name = "xmarks"
urlpatterns = [
    path("", views.indexTemplateView.as_view(), name="index"),
    path("tags/<int:pk>/", views.tagDetailView.as_view(), name="tag-detail"),
    path(
        "bookmarks/create/",
        views.bookmarkCreateView.as_view(),
        name="bookmark-create",
    ),
    path(
        "bookmarks/<int:pk>/",
        views.bookmarkDetailView.as_view(),
        name="bookmark-detail",
    ),
    path(
        "bookmarks/",
        views.bookmarkListView.as_view(),
        name="bookmark-list",
    ),
    path(
        "categories/create/",
        views.categoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "categories/<int:pk>/",
        views.categoryDetailView.as_view(),
        name="category-detail",
    ),
    path(
        "categories/",
        views.categoryListView.as_view(),
        name="category-list",
    ),
]
