from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from xmarks.forms import CategoryForm
from xmarks.models import Bookmark, Category, Tag


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "xmarks/index.html"
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
        return context


class BookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    fields = [
        "name",
        "url",
        "favorite",
        "frequent",
        "tags",
        "category",
    ]
    model = Bookmark
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("xmarks:bookmark-list")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.created_by = user
        form.instance.updated_by = user
        return super().form_valid(form)


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name",
        "url",
        "favorite",
        "frequent",
        "tags",
        "category",
    ]
    model = Bookmark
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("xmarks:bookmark-list")

    def form_valid(self, form):
        user = self.request.user
        form.instance.updated_by = user
        return super().form_valid(form)


class BookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark
    login_url = reverse_lazy("login")
    queryset = Bookmark.objects.all().order_by("category")
    context_object_name = "bookmarks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_bookmarks"] = context["category"].bookmarks.all()
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    form_class = CategoryForm
    login_url = reverse_lazy("login")
    template_name = "xmarks/category_form.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.created_by = user
        form.instance.updated_by = user
        return super().form_valid(form)


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    login_url = reverse_lazy("login")
    queryset = Category.objects.all()
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
