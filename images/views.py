from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404, HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView, View
from django.core.urlresolvers import reverse_lazy
from .models import Post, Favorite
from .forms import UserForm


class ViewIndex(ListView):
    template_name = 'images/index.html'
    model = Post
    paginate_by = 15
    context_object_name = 'allPosts'


class ViewFavorites(ListView):
    template_name = 'images/favorites.html'
    model = Favorite
    paginate_by = 15
    context_object_name = 'allPosts'

    def get_queryset(self):
        if self.request.user.is_authenticated():
            user = self.request.user
            return Favorite.objects.filter(isFavorite=True, user=user)
        return redirect('images:login')


class ViewDetail(DetailView):
    template_name = 'images/detail.html'
    model = Post


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'image']

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.author = self.request.user
            return super(CreatePost, self).form_valid(form)
        return redirect('images:login')


class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'image']


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('images:index')

    def get_object(self, queryset=None):
        obj = super(DeletePost, self).get_object()
        if not obj.author.pk == self.request.user.pk:
            # Can't delete the object because the user isn't the author.
            raise Http404
        return obj


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


def upVoted(request, image_id):
    message = None
    if request.user.is_authenticated():
        post = get_object_or_404(Post, pk=image_id)
        user = request.user
    else:
        return redirect('images:login')
    try:
        obj = Favorite.objects.get(post=post, user=user)
        obj.isUpVoted = not obj.isUpVoted
        obj.save()
        message = 'OK'
    except Favorite.DoesNotExist:
        obj = Favorite(post=post, user=user, isUpVoted=True, isFavorite=False)
        obj.save()
        message = 'KO'
    ctx = {'message': message}
    return HttpResponse(json.dumps(ctx), content_type='application/json')


def fav(request, image_id):
    message = None
    if request.user.is_authenticated():
        post = get_object_or_404(Post, pk=image_id)
        user = request.user
    else:
        return redirect('images:login')
    try:
        obj = Favorite.objects.get(post=post, user=user)
        obj.isFavorite = not obj.isFavorite
        obj.save()
        message = 'OK'
    except Favorite.DoesNotExist:
        obj = Favorite(post=post, user=user, isUpVoted=False, isFavorite=True)
        obj.save()
        message = 'KO'
    ctx = {'message': message}
    return HttpResponse(json.dumps(ctx), content_type='application/json')
