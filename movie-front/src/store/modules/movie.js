const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require('axios');
// import router from '../../router';
const hash = sessionStorage.getItem('jwt')
const options = {
    headers: {
        Authorization: 'JWT ' + hash
    }
}

const state = {
    movielist: [],
    movie: {},
    movieid: 100,
    ratingid: 0,
    movieerrors: [],
    ratingcount: 0,
    ratings: []
};

// Vuex 에서는 Arrow Function
const getters = {
    getMovielist: state => state.movielist,
    getMovie: state => state.movie,
    getMovieid: state => state.movieid,
    getRatingid: state => state.ratingid,
    getMovieErrors: state => state.errors,
    getRatingcount: state => state.ratingcount,
    getRatings: state => state.ratings
};

const mutations = {
    setMovielist: (state, movierecomm) => {
        state.movielist = movierecomm
    },
    setMovie: (state, moviedetail) => {
        state.movie = moviedetail
    },
    pushMovieError: (state, error) => state.movieerrors.push(error),
    setMovieid: (state, movieid) => {
        state.movieid = movieid
    },
    setRatingid: (state, ratingid) => state.ratingid = ratingid,
    setRatingcount: (state, number) => state.ratingcount = number,
    setRatings: (state, number) => state.ratings = number,
};

const actions = {
    // 전체 영화 리스트
    allMovie: ({commit}) => {
        axios.get(HOST+'api/v1/movies/')
        .then(res => {
            commit('setMovielist', res.data)
        })
        .catch(err => {
            if (!err.response) { // no reponse
                commit('pushMovieError', '네트워크가 불안정합니다.')
            } else if (err.response.status === 400) {
                commit('pushMovieError', '잘못된 정보입니다');
            } else if (err.response.status === 500) {
                commit('pushMovieError', '나중에 다시 시도해주세요.');
            } else {
                commit('pushMovieError', '알 수 없는 에러가 일어났습니다.');
            }
        })
    },
    // wishlist 추가
    addwishlist: ({ commit }, movieid) => {
        axios.post(HOST+'api/v1/movies/'+movieid+'/wishlist/', null, options)
        .then(res => {
            console.log(res)  
        })
        .catch(err => {
            if (!err.response) { // no reponse
                commit('pushMovieError', '네트워크가 불안정합니다.')
            } else if (err.response.status === 400) {
                commit('pushMovieError', '잘못된 정보입니다');
            } else if (err.response.status === 500) {
                commit('pushMovieError', '나중에 다시 시도해주세요.');
            } else {
                commit('pushMovieError', '알 수 없는 에러가 일어났습니다.');
            }
        })
    },
    deletewish: ({ commit }, movieid) => {
        axios.delete(HOST+'api/v1/movies/'+movieid+'/wishlist/', options)
        .then(res => {
            console.log(res)  
        })
        .catch(err => {
            if (!err.response) { // no reponse
                commit('pushMovieError', '네트워크가 불안정합니다.')
            } else if (err.response.status === 400) {
                commit('pushMovieError', '잘못된 정보입니다');
            } else if (err.response.status === 500) {
                commit('pushMovieError', '나중에 다시 시도해주세요.');
            } else {
                commit('pushMovieError', '알 수 없는 에러가 일어났습니다.');
            }
        })
    },
    // 유저의 평가를 db에 보낸다
    sendRating: ({ commit }, ratingdetail) => {
        const movieid = ratingdetail.movieid
        const rating = {
            like: ratingdetail.likes,
            keyword1: ratingdetail.keyword1,
            keyword2: ratingdetail.keyword2,
            comment: ratingdetail.comment
        }
        axios.post(HOST+'api/v1/movies/'+movieid+'/', rating, options)
        .then(res => {
            console.log(res.status)
        })
        .catch(err => {
            if (!err.response) { // no reponse
                commit('pushMovieError', '네트워크가 불안정합니다.')
            } else if (err.response.status === 400) {
                commit('pushMovieError', '잘못된 정보입니다');
            } else if (err.response.status === 500) {
                commit('pushMovieError', '나중에 다시 시도해주세요.');
            } else {
                commit('pushMovieError', '알 수 없는 에러가 일어났습니다.');
            }
        })
    },
    // 유저의 평가를 수정
    updateRating: ({ commit }, data) => {
        const movieid = data.movieid
        const ratingid = data.ratingid
        const rating = {
            like: data.likes,
            keyword1: data.keyword1,
            keyword2: data.keyword2,
            comment: data.comment
        }
        axios.patch(HOST+'api/v1/movies/'+movieid+'/'+ratingid+'/', rating, options)
        .then (res =>
            console.log(res.status)
        )
        .catch(err => {
            if (!err.response) { // no reponse
                commit('pushMovieError', '네트워크가 불안정합니다.')
            } else if (err.response.status === 400) {
                commit('pushMovieError', '잘못된 정보입니다');
            } else if (err.response.status === 500) {
                commit('pushMovieError', '나중에 다시 시도해주세요.');
            } else {
                commit('pushMovieError', '알 수 없는 에러가 일어났습니다.');
            }
        })
    },
    deleterating: ({ commit }, data) => {
        const movieid = data.movieid
        const ratingid = data.ratingid
        axios.delete(HOST+'api/v1/movies/'+movieid+'/'+ratingid+'/', options)
        .then (res =>
            console.log(res.status)
        )
        .catch(err => {
            if (!err.response) { // no reponse
                commit('pushMovieError', '네트워크가 불안정합니다.')
            } else if (err.response.status === 400) {
                commit('pushMovieError', '잘못된 정보입니다');
            } else if (err.response.status === 500) {
                commit('pushMovieError', '나중에 다시 시도해주세요.');
            } else {
                commit('pushMovieError', '알 수 없는 에러가 일어났습니다.');
            }
        })
    },
    // 특정 영화 정보를 db에서 가져온다
    getmoviedetail: ({ commit }, movieid) => {
        axios.get(HOST+'api/v1/movies/'+movieid+'/', options)
        .then(res => {
            commit('setMovie', res.data)
            commit('setRatings', res.data.rating_set)
            commit('setRatingcount', res.data.rating_set.length)
        })
        .catch(err => {
            if (!err.response) { // no reponse
                commit('pushMovieError', '네트워크가 불안정합니다.')
            } else if (err.response.status === 400) {
                commit('pushMovieError', '잘못된 정보입니다');
            } else if (err.response.status === 500) {
                commit('pushMovieError', '나중에 다시 시도해주세요.');
            } else {
                commit('pushMovieError', '알 수 없는 에러가 일어났습니다.');
            }
        })
    },
    // 영화 추천 리스트를 db에서 가져온다
    recommendation: ({ commit }) => {
        axios.post(HOST+'api/v1/movies/recommendations/', null, options)
        .then(res => {
            console.log(res)
            commit('setMovielist', res.data)
        })
        .catch(err => {
            if (!err.response) { // no reponse
                commit('pushMovieError', '네트워크가 불안정합니다.')
            } else if (err.response.status === 400) {
                commit('pushMovieError', '잘못된 정보입니다');
            } else if (err.response.status === 500) {
                commit('pushMovieError', '나중에 다시 시도해주세요.');
            } else {
                commit('pushMovieError', '알 수 없는 에러가 일어났습니다.');
            }
        })
    },
    // 영화 아이디 잡기
    pushtoMovie: ({ commit }, movie) => {
        commit('setMovie', movie)
    }
    

}


export default {
    state,
    getters,
    mutations,
    actions
}
