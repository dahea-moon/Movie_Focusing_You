from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'genre1', 'genre2')
        # fields = ('id', 'username', 'password', 'email', 'genre1', 'genre2', 'keyword1', 'keyword2', 'wishlist', 'watchedlist', 'rates')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'keyword1', 'keyword2', 'genre1', 'genre2', 'wishlist', 'watchedlist', 'rates')