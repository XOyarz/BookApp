from twitch_app.models import TwitchUser
from twitch_app.serializers import UserSerializer
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from bookt.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = TwitchUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        from twitch_app.helper import get_twitch_user_bio

        print(serializer.validated_data['name'])
        bio = get_twitch_user_bio(serializer.validated_data['name'])
        serializer.validated_data['bio'] = bio
        serializer.save()