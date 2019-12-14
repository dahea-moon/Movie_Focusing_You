from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from movies.models import Keyword, Genre, Movie, Rating


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, default=False)
    email = models.CharField(max_length=100, unique=True, default=False)
  
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
    wishlist = models.ManyToManyField(Movie, blank=True, related_name='wished_users')
    watchedlist = models.ManyToManyField(Movie, blank=True, related_name='watched_users')
    rates = models.ManyToManyField(Movie, blank=True, through='movies.Rating', related_name='rated_user')

    # def wishlist_content(self):
    #     for wish in self.wishlist:
    #         return 

    def keyword1_content(self):
        if self.keyword1:
            return Keyword.objects.get(id=self.keyword1.id).content

    def keyword2_content(self):
        if self.keyword2:
            return Keyword.objects.get(id=self.keyword2.id).content

    def genre1_name(self):
        return Genre.objects.get(id=self.genre1.id).name

    def genre2_name(self):
        return Genre.objects.get(id=self.genre2.id).name

    def get_absolute_url(self):
        return reverse("accounts:user_page", kwargs={"user_id": self.pk})

    def __str__(self):
        return self.username
