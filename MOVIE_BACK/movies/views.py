from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated


from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.core import serializers

from accounts.models import User
from .models import Movie, Rating, Keyword
from accounts.serializers import UserSerializer
from .serializers import MovieSerializer, RatingSerializer, RatingCreationSerializer

from django.db.models import Q
from django.db.models import Count

from IPython import embed

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


def update_user_keyword(request):
    user = request.user

    keyword1_list = Rating.objects.filter(user_id=user.id).values('keyword1').annotate(key_cnt=Count('keyword1')).order_by('-key_cnt')
    keyword2_list = Rating.objects.filter(user_id=user.id).values('keyword2').annotate(key_cnt=Count('keyword2')).order_by('-key_cnt')

    key_cnts = {}
    for keyword in keyword1_list:
        if keyword.get('keyword1') in key_cnts.keys():
            key_cnts[keyword['keyword1']] += keyword['key_cnt']
        else:
            key_cnts[keyword['keyword1']] = keyword['key_cnt']
    for keyword in keyword2_list:
        if keyword.get('keyword2') in key_cnts.keys():
            key_cnts[keyword['keyword2']] += keyword['key_cnt']
        else:
            key_cnts[keyword['keyword2']] = keyword['key_cnt']

    import collections
    sorted_cnts = sorted(key_cnts.items(), key=lambda kv: kv[1], reverse=True)
    sorted_key_cnts = collections.OrderedDict(sorted_cnts)
    sorted_key_cnts_keylist = list(sorted_key_cnts)

    keyword1 = sorted_key_cnts_keylist[0]
    keyword2 = sorted_key_cnts_keylist[1]
    
    serializer = UserSerializer(instance=user, data={'keyword1':keyword1, 'keyword2':keyword2}, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200, data={'message': '평점 작성 성공'})


def update_movie_keyword(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    keyword1_list = Rating.objects.filter(movie_id=movie.id).values('keyword1').annotate(key_cnt=Count('keyword1')).order_by('-key_cnt')
    keyword2_list = Rating.objects.filter(movie_id=movie.id).values('keyword2').annotate(key_cnt=Count('keyword2')).order_by('-key_cnt')
    
    key_cnts = {}
    for keyword in keyword1_list:
        if keyword.get('keyword1') in key_cnts.keys():
            key_cnts[keyword['keyword1']] += keyword['key_cnt']
        else:
            key_cnts[keyword['keyword1']] = keyword['key_cnt']
    for keyword in keyword2_list:
        if keyword.get('keyword2') in key_cnts.keys():
            key_cnts[keyword['keyword2']] += keyword['key_cnt']
        else:
            key_cnts[keyword['keyword2']] = keyword['key_cnt']

    import collections
    sorted_cnts = sorted(key_cnts.items(), key=lambda kv: kv[1], reverse=True)
    sorted_key_cnts = collections.OrderedDict(sorted_cnts)
    sorted_key_cnts_keylist = list(sorted_key_cnts)

    keyword1 = sorted_key_cnts_keylist[0]
    keyword2 = sorted_key_cnts_keylist[1]
    keyword3 = sorted_key_cnts_keylist[2]
    
    serializer = MovieSerializer(instance=movie, data={'keyword1':keyword1, 'keyword2':keyword2, 'keyword3':keyword3}, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200, data={'message': '평점 작성 성공'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_recommendations(request):
    user = request.user
    genre1 = user.genre1
    genre2 = user.genre2
    keyword1 = user.keyword1
    keyword2 = user.keyword2

    query = Q(keyword1=keyword1) & Q(keyword2=keyword2)

    watched = user.watchedlist.all().values('id')
    movies_set = Movie.objects.exclude(id__in=watched).filter(query)

    if movies_set.count() > 8:
        movies_set = movies_set.random(8)

    else:
        query.add(Q(keyword1=keyword2) & Q(keyword2=keyword1), Q.OR)
        movies_set = Movie.objects.exclude(id__in=watched).filter(query)

        if movies_set.count() < 8:
            query.add(Q(keyword1=keyword1) | Q(keyword2=keyword1), Q.OR)
            movies_set = Movie.objects.exclude(id__in=watched).filter(query)

        if movies_set.count() < 8:
            query.add(Q(keyword1=keyword2) | Q(keyword2=keyword2), Q.OR)
            movies_set = Movie.objects.exclude(id__in=watched).filter(query)

        if movies_set.count() < 8:
            query.add(Q(genre1=genre1) & Q(genre2=genre2), Q.OR)
            movies_set = Movie.objects.exclude(id__in=watched).filter(query)

        if movies_set.count() < 8:
            query.add(Q(genre1=genre2) & Q(genre2=genre1), Q.OR)
            movies_set = Movie.objects.exclude(id__in=watched).filter(query)

        if movies_set.count() < 8:
            query.add(Q(genre1=genre1) | Q(genre2=genre1), Q.OR)
            movies_set = Movie.objects.exclude(id__in=watched).filter(query)

        if movies_set.count() < 8:
            query.add(Q(genre1=genre2) | Q(genre2=genre2), Q.OR)
            movies_set = Movie.objects.exclude(id__in=watched).filter(query)

        movies_set = Movie.objects.exclude(id__in=watched).filter(query)[:8]
    serializer = MovieSerializer(movies_set, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Rating 생성
    if request.method == 'POST':
        user = request.user
        rating = RatingCreationSerializer(data=request.data)
        if rating.is_valid(raise_exception=True):
            rating.save(movie=movie, user=user)
            update_movie_keyword(request, movie.id)
            update_user_keyword(request)
            user.watchedlist.add(movie_id)
            user.wishlist.remove(movie_id)
            return Response(status=200, data={'message': '평점 작성 성공'})
    elif request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def rating_detail(request, movie_id, rating_id):
    # embed()
    rating = get_object_or_404(Rating, id=rating_id)
    user = request.user
    if rating.user == user:
        if request.method == 'PATCH':
            serializer = RatingSerializer(
                instance=rating,
                data=request.data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                update_user_keyword(request)
                update_movie_keyword(request, movie_id)
                return Response(serializer.data)
            return Response(status=400, data=serializer.errors)
        elif request.method == 'DELETE':
            rating.delete()
            user.watchedlist.remove(movie_id)
            update_user_keyword(request)
            update_movie_keyword(request, movie_id)
            return Response(status=204)
    return Response(status=403)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def wishlist(request, movie_id):
    user = request.user
    if request.method == 'POST':
        user.wishlist.add(movie_id)
        return Response(status=200, data={'message':'보고 싶은 영화 추가 성공!'})
    elif request.method == 'DELETE':
        user.wishlist.remove(movie_id)
        return Response(status=200, data={'message':'보고 싶은 영화 삭제!'})


# def search(request):
    # pass