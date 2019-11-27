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
    -   R : GET
    -   U: PATCH
    -   D : DELETE

## Movies

-   Movie List
    -   전체 리스트
        -   GET ``api/v1/movies/``
    -   추천
        -   POST ``api/v1/movies/recommendations/``

-   Movie Detail
    -   ``api/v1/movies/<int:movie_id>/``
    -   R : GET
    -   C : POST => Rating 생성
    -   U : PATCH
    -   D : DELETE