from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def index(request):
    allPosts = Post.objects.all()
    paginator = Paginator(allPosts.order_by('pk'), 15)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {'allPosts': post}
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

def detailedFaved(request, image_id):
    post = get_object_or_404(Post, pk=image_id)
    post.isFaved = not post.isFaved
    post.save()
    return render(request, 'images/detail.html', {'post': post})

def generalFaved(request, image_id):
    post = get_object_or_404(Post, pk=image_id)
    post.isFaved = not post.isFaved
    post.save()
    return HttpResponseRedirect("/images/")

