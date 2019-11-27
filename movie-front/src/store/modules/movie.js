const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require('axios');
// import router from '../../router';

const state = {
    movielist: [],
    movie: {},
    movieid: 0,
    movieerrors: []
};

// Vuex 에서는 Arrow Function
const getters = {
    getMovielist: state => state.movielist,
    getMovie: state => state.movie,
    getMovieid: state => state.movieid,
    getMovieErrors: state => state.errors
};

const mutations = {
    setMovielist: (state, movierecomm) => {
        state.movielist = movierecomm
    },
    setMovie: (state, moviedetail) => {
        state.movie = moviedetail
    },
    pushMovieError: (state, error) => state.movieerrors.push(error),
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
    // 유저의 평가를 db에 보낸다
    // 특정 영화 정보를 db에서 가져온다

    // 영화 추천 리스트를 db에서 가져온다
    recommendation: ({ commit }) => {
        const hash = sessionStorage.getItem('jwt')
        const options = {
            headers: {
                Authorization: 'JWT ' + hash
            }
        }
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
    }
    // 영화를 서치한다
}


export default {
    state,
    getters,
    mutations,
    actions
}
