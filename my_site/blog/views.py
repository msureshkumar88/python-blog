from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]


class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


class PostDetailsView(DetailView):
    template_name = "blog/post-details.html"
    model = Post
