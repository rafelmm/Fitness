from django.conf.urls import url
from fitapp import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^user/list/$', views.UserListView.as_view(), name='user_list'),
    url(r'^user/(?P<pk>\d+)/$', views.UserDetailView.as_view(), name='user_detail'),
    url(r'^user/create/$', views.UserCreateView, name='user_create'),
    url(r'^user/create_action/$', views.user_create_action, name='user_create_action'),
    url(r'^user/(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(), name='user_update'),
    url(r'^user/(?P<usuario_id>\d+)/update_action/$', views.user_update_action, name='user_update_action'),
    url(r'^address/(?P<pk>\d+)/update/$', views.AddressUpdateView.as_view(), name='address_update'),
    url(r'^address/(?P<direccion_id>\d+)/update_action/$', views.address_update_action, name='address_update_action'),
]
