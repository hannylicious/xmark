from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from xmarks.forms import BookmarkForm
from xmarks.models import Bookmark, Tag


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "xmarks/home.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookmarks"] = Bookmark.objects.filter(user=self.request.user)
        context["favorite_bookmarks"] = context["bookmarks"].filter(
            favorite=True
        )
        context["frequent_bookmarks"] = context["bookmarks"].filter(
            frequent=True
        )
        return context


class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_bookmarks"] = context["tag"].bookmark_set.all(
            user=self.request.user
        )
        return context


class BookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    """View for creating Bookmarks."""

    model = Bookmark
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("xmarks:bookmark-list")
    form_class = BookmarkForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.created_by = user
        form.instance.updated_by = user
        return super().form_valid(form)


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    """View for updating Bookmarks."""

    model = Bookmark
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("xmarks:bookmark-list")
    form_class = BookmarkForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.updated_by = user
        return super().form_valid(form)


class BookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark
    login_url = reverse_lazy("login")
    context_object_name = "bookmarks"

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).order_by("tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
