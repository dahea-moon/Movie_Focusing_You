from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny  # 회원가입은, 인증을 볼 필요가 없음.


from rest_framework.response import Response  # json 응답 생성기
from rest_framework.decorators import api_view  # require_methods
from django.shortcuts import render
from django.core import serializers

from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

from django.db.models import Q
from django.db.models import Count

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
@permission_classes([AllowAny])
def movie_recommendations(request):
    
    user = request.user
    genre1 = user.genre1
    genre2 = user.genre2
    
    """
    1. user_main_key, user_sub_key 모두 만족하는 영화
    2. user_main_key, user_sub_key 둘 중 하나만 만족하는 영화
    3. user main_genre, sub_genre 둘 다 만족
    4. user main_genre, sub_genre 둘 중 하나만 만족

    """
    # TODO user keyword 계산해서 가져오기!
    query = Q(genre1=genre1) | Q(genre2=genre1)
    query.add(Q(genre1=genre2) | Q(genre2=genre2), Q.OR)
    
    fieldname = 'keyword1'
    keyword1_list = Rating.objects.values('keyword1').annotate(key_cnt=Count('keyword1')).order_by('-key_cnt')
    keyword2_list = Rating.objects.values('keyword2').annotate(key_cnt=Count('keyword1')).order_by('-key_cnt')

    print('/////////////////////////////////////////////////////////')
    print(keyword1_list)
    print(keyword2_list)
    print('/////////////////////////////////////////////////////////')
    
    key_cnts = {}
    for keyword in keyword1_list:
        if keyword.keyword1 in key_cnts.keys:
            key_cnts.keys += keyword.key_cnt
        else:
            key_cnts[keyword.keyword1] = keyword.key_cnt
    print(key_cnts)


    

    # keyword1_list = Rating.objects.values('keyword1').annotate(key_cnt=Count('keyword1')).order_by('key_cnt')[0]
    # if keyword1_list:
    #     keyword1 = keyword1_list[0]
    #     print(keyword1, '++++')

    # query.add(Q(keyword1=keyword1) | Q(keyword2=keyword1), Q.OR)

    # keyword2 = Rating.objects.values('keyword2').annotate(key_cnt=Count('keyword2')).order_by('key_cnt')[0]

    # query.add(Q(keyword1=keyword2) | Q(keyword2=keyword2), Q.OR)
    
    movies_set = Movie.objects.filter(query)
    
    if movies_set.count() > 5:
        movies_set = movies_set.random(5)
    serializer = MovieSerializer(movies_set, many=True)
    return Response(serializer.data)


# TODO : KEYWORD column 추가, watchedlist 추가
@api_view(['GET', 'POST'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Rating 생성
    if request.method == 'POST':
        user = request.user
        rating = RatingSerializer(data=request.data)
        if rating.is_valid(raise_exception=True):
            rating.save()
            return Response(status=200, data={'message': '평점 작성 성공'})

        # 생성한 후에 해당 유저와 해당 영화의 베스트 키워드 순위 집계 후 탑 2 를 갱신

    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['PATCH', 'DELETE'])
def rating_detail(request, movie_id, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    if rating.user == request.user:
        if request.method == 'PATCH':
            serializer = RatingSerializer(
                instance=rating,
                data=request.data,
                partial=True
            )
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
    # TODO user.wishlist [] 에 movie_id 추가만!
    user.save()
    return Response(status=200, message='보고 싶은 영화 추가 성공!')


def add_watched_movie(request, movie_id):
    pass

def search_movies(request):
    pass