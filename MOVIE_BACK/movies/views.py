from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.response import Response  # json 응답 생성기
from rest_framework.decorators import api_view  # require_methods
from django.shortcuts import render  

from .models import Movie
from .serializers import MovieSerializer, RatingSerializer


def movie_list(request):
    pass


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



@api_view(['PATCH', 'DELETE'])
def rating_detail(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)

    if request.method == 'PATCH':
        serializer = RatingSerializer(instance=rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400, data=serializer.errors)

    elif request.method == 'DELETE':
        rating.delete()
        return Response(status=204)




# def update_user_keyword(request):
#     pass

# def update_movie_keyword(request):
#     pass

