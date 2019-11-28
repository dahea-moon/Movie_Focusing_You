from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Rating, Movie

User = get_user_model()


class RatingCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ['user', 'movie']


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    rating_set = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
