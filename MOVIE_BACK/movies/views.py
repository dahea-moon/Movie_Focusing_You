from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.response import Response  # json 응답 생성기
from rest_framework.decorators import api_view  # require_methods
from django.shortcuts import render
from django.core import serializers


from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# TODO : KEYWORD column 추가, watchedlist 추가
@api_view(['POST'])
def create_rating(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie.id, user_id=user.id)
    return Response(serializer.data)


@api_view(['PATCH', 'DELETE'])
def rating_detail(request, movie_id, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    if rating.user == request.user:
        if request.method == 'PATCH':
            serializer = RatingSerializer(instance=rating, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(status=400, data=serializer.errors)
        elif request.method == 'DELETE':
            rating.delete()
            return Response(status=204)
    return Response(status=403)


def update_user_keyword(request):
    pass


def update_movie_keyword(request):
    pass


def wishlist(request):
    pass
