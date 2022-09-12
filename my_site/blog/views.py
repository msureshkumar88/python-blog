from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
# Create your views here.


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]


def posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {
        "posts": posts
    })


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-details.html", {
        "post": post,
        "tags": post.tags.all()
    })
