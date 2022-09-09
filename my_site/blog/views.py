from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def posts(request):
    return render(request, "blog/posts.html")


def post_details(request, slug):
    return render(request, "blog/post-details.html")

