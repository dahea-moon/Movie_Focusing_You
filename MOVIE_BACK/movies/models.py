from django.db import models
# from django.contrib.auth import get_user_model
# settings.AUTH_USER_MODEL = get_user_model()

from django.urls import reverse

from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Keyword(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.content}'


class Movie(models.Model):
    title = models.CharField(max_length=100, default='')
    titleEng = models.CharField(max_length=100, default='')
    director = models.CharField(max_length=50, default='')
    actors = models.CharField(max_length=100, default='')
    nation = models.CharField(max_length=50, default='')
    plot = models.TextField()
    runtime = models.CharField(max_length=50, default='')
    genre1 = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_main_genre'
        )
    genre2 = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_sub_genre'
        )
    ratingGrade = models.CharField(max_length=50, default='')
    releaseDt = models.CharField(max_length=50, default='')
    descriptions = models.CharField(max_length=100, default='')
    poster = models.CharField(max_length=100, default='')
    stills = models.TextField()
    awards = models.TextField()
    keyword1 = models.ForeignKey(
        Keyword,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_main_keyword'
        )
    keyword2 = models.ForeignKey(
        Keyword,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_sub_keyword1'
        )
    keyword3 = models.ForeignKey(
        Keyword,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movie_sub_keyword2'
        )

    def __str__(self):
        return f'{self.id}: {self.title}'


class Movie_Keyword(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}=> movie: {self.movie} keyword: {self.keyword}'


class User_Keyword(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}=> user: {self.user} keyword: {self.keyword}'


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.BooleanField()
    comment = models.CharField(max_length=100)
    keyword1 = models.ForeignKey(Keyword, null=True, on_delete=models.SET_NULL, related_name='rating_main_keword')
    keyword2 = models.ForeignKey(Keyword, null=True, on_delete=models.SET_NULL, related_name='rating_sub_keyword')

    # TODO 얘네는 사용자가 등록하느느 것이 아닌 자동으로 해당하느느 model의 object 를 생성 후 여기에 저장된다.
    # user_key1 = models.ForeignKey(User_Keyword, null=False, on_delete=models.CASCADE, related_name='rating_main_keyword')
    # user_key2 = models.ForeignKey(User_Keyword, null=False, on_delete=models.CASCADE, related_name='rating_sub_keyword')
    # mov_key1 = models.ForeignKey(Movie_Keyword, null=False, on_delete=models.CASCADE, related_name='rating_main_keyword')
    # mov_key2 = models.ForeignKey(Movie_Keyword, null=False, on_delete=models.CASCADE, related_name='rating_sub_keyword')

    def __str__(self):
        return f'{self.id}: {self.comment}'


