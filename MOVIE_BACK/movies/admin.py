from django.contrib import admin
from .models import Movie, Genre, Keyword, Rating

admin.site.register(Movie)
admin.site.register(Keyword)
admin.site.register(Genre)
admin.site.register(Rating)
