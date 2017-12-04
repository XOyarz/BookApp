from rest_framework import serializers
from bookt.models import Book, UserProfile
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('owner', 'title', 'author', 'description', 'picture', 'image_url', 'created')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'country', 'city', 'zipcode', 'lat', 'lng')

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'books')