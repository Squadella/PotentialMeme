from django.conf.urls import url
from . import views

urlpatterns = [
    # /images/
    url(r'^$', views.index, name='index'),

    # /images/imageID
    url(r'^(?P<image_id>[0-9]+)/$',views.postDetail , name='detail'),
]
