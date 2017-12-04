from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bookt import views

urlpatterns = [
    url(r'^book/$', views.BookList.as_view()),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
]