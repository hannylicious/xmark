from django.urls import path

from . import views

app_name = "xmarks"
urlpatterns = [
    path("", views.IndexTemplateView.as_view(), name="index"),
    path("tags/<int:pk>/", views.TagDetailView.as_view(), name="tag-detail"),
    path(
        "bookmarks/create/",
        views.BookmarkCreateView.as_view(),
        name="bookmark-create",
    ),
    path(
        "bookmarks/<int:pk>/",
        views.BookmarkDetailView.as_view(),
        name="bookmark-detail",
    ),
    path(
        "bookmarks/update/<int:pk>/",
        views.BookmarkUpdateView.as_view(),
        name="bookmark-update",
    ),
    path(
        "bookmarks/",
        views.BookmarkListView.as_view(),
        name="bookmark-list",
    ),
]
