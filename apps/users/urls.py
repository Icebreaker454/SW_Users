from django.conf.urls import url

from apps.users.views import UserListView

urlpatterns = [
    url(r'^$', UserListView.as_view(), name='user_list'),
]
