from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from bookt import views

urlpatterns = [
    url(r'^book/$', views.BookList.as_view(), name='book-list'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^$', views.api_root)
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]