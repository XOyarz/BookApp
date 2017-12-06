from rest_framework import serializers
from twitch_app.models import TwitchUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchUser
        fields = ('id', 'name', 'bio', 'game', 'followers', 'views', 'profile_link')