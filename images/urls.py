from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'images'

urlpatterns = [
    # /images/
    url(r'^$', views.ViewIndex.as_view(), name='index'),

    # /images/favorites/
    url(r'^favorites/$', views.ViewFavorites.as_view(), name='favorites'),

    # /images/register/
    url(r'^register/$', views.UserFormRegistration.as_view(), name='register'),

    # /images/login
    url(r'^login/$', views.UserFormLogin.as_view(), name='login'),

    # /images/logout
    url(r'^logout/$', views.userLogout, name='logout'),

    # /images/pk
    url(r'^(?P<pk>[0-9]+)/$', views.ViewDetail.as_view(), name='detail'),

    # /images/image/create/
    url(r'image/create/$', views.CreatePost.as_view(), name='CreatePost'),

    # /images/image/pk/
    url(r'image/(?P<pk>[0-9]+)/$', views.UpdatePost.as_view(), name='UpdatePost'),

    # /images/image/pk/delete
    url(r'image/(?P<pk>[0-9]+)/delete$', views.DeletePost.as_view(), name='DeletePost'),

    # /images/imageID/upVote
    url(r'(?P<image_id>[0-9]+)/upVote/$', views.upVoted, name='upVoted'),

    # /images/imageID/fav
    url(r'(?P<image_id>[0-9]+)/fav/$', views.fav, name='fav'),

]

