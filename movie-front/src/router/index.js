import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Signup from '../views/Signup.vue'
import Main from '../views/Main.vue'
import Mypage from '../views/Mypage.vue'
import Detail from '../views/Detail.vue'
import All from '../views/All.vue'

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
  {
    path: '/detail',
    name: 'detail',
    component: Detail
  },
  {
    path: '/all',
    name: 'all',
    component: All
  },
]

const router = new VueRouter({
  mode: 'history', // url에 '#' 없애기
  routes
})

export default router
