from django.shortcuts import render
from .models import Post
# from the current folder that we are in inside models import post

# Create your views here.
def post(request):
    blog_posts = Post.objects.all()
    context = {
        "blog_posts": blog_posts,

    }
    return render(request, 'post.html', context)

def postdetails(request, id):
    post = Post.objects.get(id = id)
    context = {
        "post": post
    }
    return render(request, 'postdetails.html', context)