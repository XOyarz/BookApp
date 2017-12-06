from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from twitch_app import views

urlpatterns = [
    url(r'^twitch/$', views.UserList.as_view()),
    url(r'^twitch/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

]