from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Rating, Movie

User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ()

class RatingCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('__all__')

