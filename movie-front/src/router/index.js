import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Signup from '../views/Signup.vue'
import Main from '../views/Main.vue'
import Mypage from '../views/Mypage.vue'

Vue.use(VueRouter) // 우리 같이 일해보자. 악수.

const routes = [
  {
    path: '/',
    name: 'main',
    component: Main
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: Mypage
  },
]

const router = new VueRouter({
  mode: 'history', // url에 '#' 없애기
  routes
})

export default router
