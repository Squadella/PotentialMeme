from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'images'

urlpatterns = [
    # /images/
    url(r'^$', views.index, name='index'),

    # /images/imageID
    url(r'^(?P<image_id>[0-9]+)/$', views.postDetail, name='detail'),

    # /images/imageID/favorite
    url(r'^(?P<image_id>[0-9]+)/favorite/$', views.detailedUpVoted, name='detailedUpVoted'),

    # /images/imageID/fav
    url(r'^(?P<image_id>[0-9]+)/fav/$', views.generalUpVoted, name='generalUpVoted'),
]
