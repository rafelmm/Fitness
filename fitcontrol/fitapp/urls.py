from django.conf.urls import url
from fitapp import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'user/(?P<pk>\d+)/$', views.UserDetailView.as_view(), name='user_detail'),
    url(r'address/$', views.address_list, name='address_list'),
    url(r'^user/(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(), name='user_update'),
    url(r'^user/(?P<usuario_id>\d+)/update_action/$', views.user_update_action, name='user_update_action'),
]
