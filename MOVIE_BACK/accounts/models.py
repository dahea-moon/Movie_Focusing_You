from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from movies.models import Keyword, Genre, Movie, Rating


class User(AbstractUser):
    keyword1 = models.ForeignKey(
        Keyword,
        null=True,
        on_delete=models.SET_NULL,
        related_name='user_main_keyword'
        )
    keyword2 = models.ForeignKey(
        Keyword,
        null=True,
        on_delete=models.SET_NULL,
        related_name='user_sub_keyword'
        )
    genre1 = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name='user_main_genre'
        )
    genre2 = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name='user_sub_genre'
        )
    wishlist = models.ManyToManyField(Movie, related_name='wished_users')
    watchedlist = models.ManyToManyField(Movie, related_name='watched_users')
    rates = models.ManyToManyField(Movie, through='movies.Rating', related_name='rated_user')

    def get_absolute_url(self):
        return reverse("accounts:user_page", kwargs={"user_id": self.pk})

    def __str__(self):
        return self.username
