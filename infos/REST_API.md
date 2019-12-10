# REST API

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/movies/', include('movies.urls')),
]
```



## Accounts

-   Signup
    -   POST : ``api/v1/accounts/signup``
-   User Detail
    -   ``api/v1/accounts/mypage/``
    -   GET : 유저 정보 조회
    -   PATCH : 유저 정보 수정
    -   DELETE : 유저 삭제

## Movies

-   Movie List
    -   전체 영화 리스트 보기
        -   GET ``api/v1/movies/``
    -   유저 맞춤 추천 영화 리스트 보기
        -   POST ``api/v1/movies/recommendations/``

-   Movie Detail

    -   ``api/v1/movies/<int:movie_id>/``
        -   GET : 영화 상세 정보 보기
        -   PATCH : 영화 정보 수정
        -   DELETE : 영화 삭제 

-   Rating

    -   작성
        -   POST ``api/v1/movies/<int:movie_id>/``
        -   PATCH ``api/v1/movies/<int:movie_id>/<int:rating_id>/``
        -   DELETE ``api/v1/movies/<int:movie_id>/<int:rating_id>/``

-   Wishlist 추가

    -   ``api/v1/movies/<int:movie_id>/wishlist/``
        -   POST : 위시리스트 추가
        -   DELETE : 위시리스트 제거

    