from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/posts.html")


def post_details(request, slug):
    return render(request, "blog/post-details.html")

# 5.10