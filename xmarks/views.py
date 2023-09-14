from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    TemplateView,
    UpdateView,
)

from xmarks.forms import CategoryForm
from xmarks.models import Tag, Bookmark, Category


class indexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "xmarks/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookmarks"] = Bookmark.objects.filter(user=self.request.user)
        context["favorite_bookmarks"] = context["bookmarks"].filter(is_favorite=True)
        return context


class tagDetailView(LoginRequiredMixin, DetailView):
    model = Tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class bookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class bookmarkCreateView(LoginRequiredMixin, CreateView):
    fields = [
        "name",
        "url",
        "is_favorite",
        "tags",
        "category",
    ]
    model = Bookmark
    success_url = reverse_lazy("xmarks:bookmark-list")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.created_by = user
        form.instance.updated_by = user
        return super().form_valid(form)


class bookmarkUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name",
        "url",
        "is_favorite",
        "tags",
        "category",
    ]
    model = Bookmark
    success_url = reverse_lazy("xmarks:bookmark-list")

    def form_valid(self, form):
        user = self.request.user
        form.instance.updated_by = user
        return super().form_valid(form)


class bookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark
    queryset = Bookmark.objects.all().order_by("category")
    context_object_name = "bookmarks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class categoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_bookmarks"] = context["category"].bookmarks.all()
        return context


class categoryCreateView(LoginRequiredMixin, CreateView):
    form_class = CategoryForm
    template_name = "xmarks/category_form.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.created_by = user
        form.instance.updated_by = user
        return super().form_valid(form)


class categoryListView(LoginRequiredMixin, ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
