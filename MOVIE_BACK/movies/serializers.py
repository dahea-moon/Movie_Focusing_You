from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Rating, Movie

User = get_user_model()


class RatingCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ['user', 'movie']


class RatingSerializer(serializers.ModelSerializer):
    k1_content = serializers.CharField(source='keyword1_content')
    k2_content = serializers.CharField(source='keyword2_content')

    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = (
            'k1_content',
            'k2_content',
        )


class MovieSerializer(serializers.ModelSerializer):
    rating_set = RatingSerializer(many=True)
    g1_name = serializers.CharField(source='genre1_name')
    g2_name = serializers.CharField(source='genre2_name')
    k1_content = serializers.CharField(source='keyword1_content')
    k2_content = serializers.CharField(source='keyword2_content')
    k3_content = serializers.CharField(source='keyword3_content')
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = (
            'k1_content',
            'k2_content',
            'k3_content',
            'g1_name',
            'g2_name',
        )
