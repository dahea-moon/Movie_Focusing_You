## 네이버 영화 API

### 요청키

- query: 필수 // 검색을 원하는 질의
- display: 검색 결과 출력 건수
- start: 검색의 시작 위치를 지정
- genre: 장르 코드
- country: 국가 코드
- yearfrom: 제작년도(최소)
- yearto: 제작년도(최대)

### 출력 결과

- rss
- chanenl: 검색 결과를 포함하는 컨테이너
- lastBuildDate: 검색 결과 생성 시간
- items: 개별 검색 결과
  - title
  - link: 영화의 하이퍼텍스트 link
  - image: 썸네일 이미지의 URL
  - subtitle: 영문 제목
  - pubDate: 제작년도
  - director: 감독
  - actor: 출연배우
  - userRating: 유저들의 평점

### KMDB API

### 요청인자

- ServiceKey:  필수 // 서비스 인증키
- listCount; 통합검색 출력 결과수
- startCount: 검색 결과 시작 번호
- collection: 검색대상 컬렉션 지정
- query: 검색 질의어
- detail: 상세정보 출력 여부
- sort: 결과 정렬 (정확도순, 영화명, 감독명, 제작사명, 제작년도)
- createDts: 제작년도 시작
- createDte: 제작년도 종료
- releaseDts: 개봉일 시작
- releaseDte: 개봉일 종료
- nation: 국가명
- company: 제작사명
- genre: 장르명
- ratedYn: 심의여부
- use: 용도구분
- movieId
- movieSeq
- type: 유형명
- title: 영화명
- director: 감독명
- actor: 배우명
- staff: 스탭명
- keyword: 키워드
- plot: 줄거리

### 출력결과:

- Result: collection명, 검색결과 시작, 화면에 노출될 결과개수, 총결과수
- Row Value: 검색결과 리스트 내 일련번호
- docid: pk
- movieId: 등록 id
- movieSeq: 등록 seq
- title: 영화명
- titleeng
- titleorg
- titleetc: 기타제명
- directorNm: 감독명
- directorId: 감독 등록번호
- actorNm: 배우명
- actorId: 배우 등록번호
- nation: 제작국가
- company: 제작사
- prodYear: 제작년도
- plot: 줄거리
- runtime: 대표 상영시간
- rating: 관람등급
- genre: 장르
- kmdbUrl: 링크 Url
- type: 유형구분
- use: 용도 구분
- episode
- ratedYn: 심의여부
- repRlsDate: 대표개봉일
- ratingGrade: 관람기준
- releaseDate: 개봉일자
- keywords: 키워드
- posterUrl: 포스터 이미지 url
- stillUrl: 스틸 이미지 url
- audiAcc: 누적관람인원
- soundtrack: 삽입곡
- awards1: 영화제수상내역
- awards2: 수상내역 기타

## 영화진흥위원회



-   영화 목록

    -   요청인터페이스

        -   key
        -   영화명
        -   감독명
        -   개봉연도
        -   제작연도
        -   국적
        -   영화유형코드

    -   응답 구조

        -   영확코드

        -   영화명

        -   제작연도

        -   개봉연도

        -   영화유형

        -   제작국가

        -   영화장르

        -   영화감독

            

-   영화상세정보

    -   요청 인터페이스
        -   key / 발급받은 키 값
        -   영화코드 / movieCd
    -   응답구조
        -   movieInfoResult
            -   movieInfo
                -   영화 코드 / movieCd
                -   영화명(국문) / movieNm          
                -   영화명(영문) / movieNmEn          
                -   영화명(원문) / movieNmOg (blank 있음)  
                -   제작연도 / prdtYear          
                -   상영시간 / showTm          
                -   개봉연도 / openDt          
                -   제작국가 / nations
                    -   제작국가명 / nationNm          
                -   genres
                    -   장르명 / genreNm (여러개)    
                -   감독 / directors
                    -   감독명 / peopleNm
                    -   감독명(원문) / peopleNmEn          
                -   배우 / actors (여러개)
                    -   배우명 / peopleNm          
                    -   배우명(영문) / peopleNmEn          
                    -   배역명 / cast          
                    -   배역명(영문) / castEn
                -   심의정보 / audits          
                    -   심의번호 / auditNo          
                    -   관람등급 / watchGradeNm



## 한국영상자료원

-   영화정보 Open API에서는 한국영화의 **제명, 제작년도, 제작사, 크레딧, 줄거리, 장르, 키워드 등** 상세정보를 제공