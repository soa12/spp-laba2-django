from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.image_list, name='index'),
    url(r'^image/(?P<image_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^image/(dis)?like/(?P<image_id>[0-9]+)/$', views.vote, name='vote'),
    url(r'^images/statistics/$', views.statistics, name='statistics'),
]

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]