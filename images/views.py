from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, DetailView
from .models import Post


class ViewIndex(ListView):
    template_name = 'images/index.html'
    model = Post
    paginate_by = 15
    context_object_name = 'allPosts'


class ViewDetail(DetailView):
    template_name = 'images/detail.html'
    model = Post


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