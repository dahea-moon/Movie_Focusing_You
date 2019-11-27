from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny  # 회원가입은, 인증을 볼 필요가 없음.


from rest_framework.response import Response  # json 응답 생성기
from rest_framework.decorators import api_view  # require_methods
from django.shortcuts import render
from django.core import serializers
from django.db.models import Q

from .models import Movie, Rating, User_Keyword, Movie_Keyword
from .serializers import MovieSerializer, RatingSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


def update_user_keyword(request):
    pass


def update_movie_keyword(request):
    pass

@api_view(['POST'])
def movie_suggestion(request):
    user = request.user
    genre1 = user.genre1
    genre2 = user.genre2

    # frst, second key, first-sec genre 모두 갖는 영화 추출
    query = Q(genre1=genre1) | Q(genre2=genre1)
    query.add(Q(genre1=genre2) | Q(genre2=genre2), Q.AND)
    query.add(Q(keyword1=keyword1) | Q(keyword2=keyword1), Q.AND)
    query.add(Q(keyword1=keyword2) | Q(keyword2=keyword2), Q.AND)


    if user.keyword1 != null:
        query.add(Q(genre1=genre2) | Q(genre2=genre2), Q.AND)
        keyword1 = user.keyword1
        keyword2 = user.keyword2

        movies_set = Movie.objects.filter(query)
        movies_set
        if movie_set.count() < 5:
            serializers = MovieSerialzer(movie_set, many=True)
            return Response(serializers)


# TODO : KEYWORD column 추가, watchedlist 추가
@api_view(['GET', 'POST'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Rating 생성
    if request.method == 'POST':
        user = request.user
        serializer = RatingSerializer(data=request.data)

        # U-K, M-K 모델 object 각각 생성
        user_key1 = User_Keyword.objects.create(
            user=request.user,
            keyword=request.data.keyword1
        )
        movie_key1 = Movie_Keyword.objects.create(
            movie=movie_id,
            keyword=request.data.keyword1
        )

        # 생성한 후에 해당 유저와 해당 영화의 베스트 키워드 순위 집계 후 탑 2 를 갱신








        if serializer.is_valid(raise_exception=True):

            user_key1 = User_Keyword.objects.create(user=request.user, keyword=request.data.keyword1)
            serializer.user_key1 = user_key1
            user_key2 = User_Keyword.objects.create(user=request.user, keyword=request.data.keyword2)
            serializer.user_key2 = user_key2

            mov_key1 = Movie_Keyword.objects.create(movie=movie.id, keyword=request.data.keyword1)
            serializer.mov_key1 = mov_key1
            mov_key2 = Movie_Keyword.objects.create(movie=movie.id, keyword=request.data.keyword2)
            serializer.mov_key2 = mov_key2

            # TODO 아래 같이 써주면 movie 랑 user id 제대로 들어가는지 + 이럼에도 불구하고 POSTMAN 에서는 movie / user 를 꼭 넣어 줘야하는지.
            serializer.save(movie=movie.id, user=user.id)

            # 탑 2 내보내는건 onjects all 해서 oreder by 해서 앞에 2개

            # user-key create
                # user model 의 keyword 항목을 top 2 를 계산해서 update
            # update_movie_keyword()
            # movie-key create
                # movie model 의 keyword 항목을 top 2 계산해서 update
            # update_movie_keyword()
            return Response(serializer.data)


    elif request.method == 'GET':
        serializer = MovieSerializer(movie)
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



# TODO: userpage로 이동
def add_wishlist(request, movie_id):
    user = request.user
    movies = get_object_or_404(Movie, id=movie_id)
    # user.wishlist 에 add
    user.save()
    return Response(status=200, message='보고 싶은 영화 추가 성공!')


def add_watched_movie(request, movie_id):
    pass




