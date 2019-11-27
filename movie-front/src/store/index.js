import Vuex from 'vuex'
import Vue from 'vue'
import auth from './modules/auth'
import movie from './modules/movie'

Vue.use(Vuex) // Vue에 Vuex 미들웨어 등록

const store = new Vuex.Store({
    modules: {
        auth,
        movie
    }
})

export default store