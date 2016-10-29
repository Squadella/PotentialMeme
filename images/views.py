from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post

def index(request):
    allPosts = Post.objects.all()
    context ={'allPosts': allPosts}
    return render(request, 'images/index.html', context)

def postDetail(request, image_id):
    post = get_object_or_404(Post, pk=image_id)
    return render(request, 'images/detail.html', {'post': post})

def detailedUpVoted(request, image_id):
    post = get_object_or_404(Post, pk=image_id)
    post.isUpVoted = not post.isUpVoted
    post.save()
    return render(request, 'images/detail.html', {'post': post})

def generalUpVoted(request, image_id):
    post = get_object_or_404(Post, pk=image_id)
    post.isUpVoted = not post.isUpVoted
    post.save()
    return HttpResponseRedirect("/images/")