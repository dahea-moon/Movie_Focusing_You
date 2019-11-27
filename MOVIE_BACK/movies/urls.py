
from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('recommendations/', views.movie_recommendations),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/<int:rating_id>/', views.rating_detail),

]