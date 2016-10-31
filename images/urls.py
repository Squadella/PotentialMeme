from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'images'

urlpatterns = [
    # /images/
    url(r'^$', views.ViewIndex.as_view(), name='index'),

    # /images/imageID
    url(r'^(?P<pk>[0-9]+)/$', views.ViewDetail.as_view(), name='detail'),

    # /images/imageID/UpVoted
    url(r'^(?P<image_id>[0-9]+)/upVoted/$', views.detailedUpVoted, name='detailedUpVoted'),

    # /images/imageID/UpVoted
    url(r'^(?P<image_id>[0-9]+)/gupVoted/$', views.generalUpVoted, name='generalUpVoted'),

    # /image/imageID/faved
    url(r'^(?P<image_id>[0-9]+)/Faved/$', views.detailedFaved, name='detailedFaved'),

    # /image/imageID/faved
    url(r'^(?P<image_id>[0-9]+)/gFaved/$', views.generalFaved, name='generalFaved'),

]

