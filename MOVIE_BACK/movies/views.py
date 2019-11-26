from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.response import Response  # json 응답 생성기
from rest_framework.decorators import api_view  # require_methods
from django.shortcuts import render  

from .models import Movie
from .serializers import MovieSerializer

def movie_list(request):
    pass


def movie_detail(request):
    pass


def create_rating(request):
    pass


def update_delete_rating(request):
    pass


# def update_user_keyword(request):
#     pass

# def update_movie_keyword(request):
#     pass

