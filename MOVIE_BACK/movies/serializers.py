from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Rating, Movie

User = get_user_model()


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'movie', 'user', 'like', 'comment', 'keyword1', 'keyword2']


class MovieSerializer(serializers.ModelSerializer):
    rating_set = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

