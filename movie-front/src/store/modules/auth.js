const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require('axios');
import router from '../../router';
// auth.js  인증관련 모든 State 를 작성.
// State 에 접근/변경 하는 모든 로직은 여기로.

const state = {
    token: null,
    errors: [],
    loading: false,
};

// Vuex 에서는 Arrow Function
const getters = {
    isLoggedIn: state => !!state.token, // 특정 값을 true/false 로 바꾸는 구문
    getErrors: state => state.errors,
    isLoading: state => state.loading,
};

const mutations = {
    setLoading: (state, flag) => state.loading = flag,
    setToken: (state, token) => {
        state.token = token;
        sessionStorage.setItem('jwt', token);
    },
    pushError: (state, error) => state.errors.push(error),
    clearErrors: state => state.errors = [],
};

const actions = {
    logout: ({ commit }) => {
        commit('setToken', null);
        sessionStorage.removeItem('jwt');
        router.push('/');
    },
    
    pushError({ commit }, error) {
        commit('pushError', error)
    },

    login: ({ commit, getters }, credentials) => {
        // 이미 로그인 했다면,
        // module 안에서는, getters 함수들은 computed 처럼, 리턴 값으로 존재한다. 실행 불가능 (getters.isLoggedIn() 은 Error)
        if (getters.isLoggedIn)  {
            router.push('/');
        } 
        // 로그인 안했다면
        else {
            commit('clearErrors');
            commit('setLoading', true);
            // username 없음
            if (!credentials.username) { 
                commit('pushError', "username을 입력하세요.");
                commit('setLoading', false);
            }
            // password < 8
            if (credentials.password < 8) {
                commit('pushError', "password는 8자 이상이어야 합니다.");
                commit('setLoading', false);
            }
            // 요청 start
            else {
                axios.post(HOST + 'api-token-auth/', credentials)
                    .then(token => {
                        commit('setToken', token.data.token);
                        commit('setLoading', false)
                        router.push('/');
                    })
                    .catch(err => {
                        if (!err.response) { // no reponse
                            commit('pushError', 'Network Error..')
                        } else if (err.response.status === 400) {
                            commit('pushError', 'Invalid username or password');
                        } else if (err.response.status === 500) {
                            commit('pushError', 'Internal Server error. Please try again later');
                        } else {
                            commit('pushError', 'Some error occured');
                        }
                        commit('setLoading', false);
                    })
                }
        }
    },

    signup: ({ commit, getters, dispatch }, userInfo) => {
        if (getters.isLoggedIn) {
            router.push('/');
        } else {
            if (!userInfo.username) {
                commit('pushError', "username을 입력하세요.");
            } 
            if (userInfo.password.length < 8) {
                commit('pushError', "password는 8자 이상이어야 합니다.");
            }
            if (userInfo.email.indexOf('@') === -1) {
                commit('pushError', "유효한 이메일을 입력하세요.");
            }
            if (userInfo.genre1 == userInfo.genre2) {
                commit('pushError', "장르를 중복하여 선택할 수 없습니다.");              
            }
            if (userInfo.genre1 === 0 || userInfo.genre2 === 0) {
                commit('pushError', "선호하는 장르를 선택해주세요.");
            }
            if (userInfo.password == userInfo.passwordconfirm && !getters.getErrors.length) {
                axios.post(HOST + 'api/v1/accounts/signup/', userInfo)
                .then(res => {
                    console.log(res)
                    if (res.status === 200) {
                        const credentials = {
                            username: userInfo.username,
                            password: userInfo.password
                        }
                        dispatch('login', credentials)
                        router.push('/')
                    }
                })
                .catch(err => {
                    commit('pushError', err.response)
                })
            } else {
                commit('pushError', "비밀번호를 재확인 해주세요"); 
            }
        }
    }

};

export default {
    state,
    getters,
    mutations,
    actions
}
