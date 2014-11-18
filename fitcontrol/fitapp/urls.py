from django.conf.urls import patterns, url
from fitapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'user/(?P<user_id>\d+)/$', views.user_detail, name='user_detail'),
    url(r'address/$', views.address_list, name='address_list'),
)
