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
        from twitch_app.helper import get_twitch_user


        twitch_user = get_twitch_user(serializer.validated_data['id'])
        #print(twitch_user)
        if twitch_user['description'] != '':
            serializer.validated_data['bio'] = twitch_user['description']
        if twitch_user['game'] != '':
            serializer.validated_data['game'] = twitch_user['game']
        serializer.validated_data['followers'] = twitch_user['followers']
        serializer.validated_data['name'] = twitch_user['name']
        serializer.validated_data['views'] = twitch_user['views']
        serializer.validated_data['profile_link'] = twitch_user['url']


        serializer.save()

class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = TwitchUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)