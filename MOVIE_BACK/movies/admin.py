from django.contrib import admin
from .models import Movie, Genre, Keyword, Rating, Movie_Keyword, User_Keyword

admin.site.register(Movie)
admin.site.register(Keyword)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Movie_Keyword)
admin.site.register(User_Keyword)
