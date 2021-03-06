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

    # /images/create/
    url(r'create/$', views.CreatePost.as_view(), name='CreatePost'),

    # /images/imageID/update
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdatePost.as_view(), name='UpdatePost'),

    # /images/image/pk/delete
    url(r'image/(?P<pk>[0-9]+)/delete$', views.DeletePost.as_view(), name='DeletePost'),

    # /images/imageID/upVote
    url(r'(?P<image_id>[0-9]+)/upVote/$', views.upVoted, name='upVoted'),

    # /images/imageID/fav
    url(r'(?P<image_id>[0-9]+)/fav/$', views.fav, name='fav'),

    # /images/imageID/deleteComment
    url(r'(?P<pk>[0-9]+)/deleteComment$', views.DeleteComment.as_view(), name='DeleteComment'),

    # /images/imageID/comment
    url(r'(?P<image_id>[0-9]+)/comment$', views.createComment, name='comment'),

]

