from django.conf.urls import url

from apps.users import views

urlpatterns = [
    url(r'^$', views.UserListView.as_view(), name='user_list'),
    url(r'^create/$', views.UserCreateView.as_view(), name='user_create'),
]
