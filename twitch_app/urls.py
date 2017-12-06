from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from twitch_app import views

urlpatterns = [
    url(r'^twitch/$', views.UserList.as_view())
]