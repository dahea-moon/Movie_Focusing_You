from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'genre1', 'genre2')


class UserSerializer(serializers.ModelSerializer):
    k1_content = serializers.CharField(source='keyword1_content')
    k2_content = serializers.CharField(source='keyword2_content')
    g1_name = serializers.CharField(source='genre1_name')
    g2_name = serializers.CharField(source='genre2_name')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'keyword1',
            'keyword2',
            'genre1',
            'genre2',
            'wishlist',
            'watchedlist',
            'rates',
            'k1_content',
            'k2_content',
            'g1_name',
            'g2_name',
        )
        