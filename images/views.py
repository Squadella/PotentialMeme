from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView, View
from django.core.urlresolvers import reverse_lazy
from .models import Post
from .forms import UserForm

class ViewIndex(ListView):
    template_name = 'images/index.html'
    model = Post
    paginate_by = 15
    context_object_name = 'allPosts'


class ViewDetail(DetailView):
    template_name = 'images/detail.html'
    model = Post


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'image']


class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'image']


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('images:index')

class UserFormRegistration(View):
    form_class = UserForm
    template_name = 'images/registration_form.html'

    # Display the blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # Recieve the filled out form
    def post(self, request):
        form = self.form_class(request.POST)
        # Check the info of the form
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('images:index')

        return render(request, self.template_name, {'form':form})


class UserFormLogin(View):
    form_class = UserForm
    template_name = 'images/login_form.html'

    # Display the blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # Recieve the filled out form
    def post(self, request):
        form = self.form_class(request.POST)
        username = form.data['username']
        password = form.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('images:index')

        return render(request, self.template_name, {'form':form})


def userLogout(request):
    logout(request)
    return redirect('images:index')


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