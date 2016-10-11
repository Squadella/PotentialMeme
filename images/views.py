from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    allPosts = Post.objects.all()
    context ={'allPosts' : allPosts}
    return render(request, 'images/index.html', context)

def postDetail(request, image_id):
    try:
        post = Post.objects.get(pk=image_id)
    except Post.DoesNotExist:
        raise Http404("Post not found!")
    return render(request, 'images/index.html', {'allPosts' : allPosts})