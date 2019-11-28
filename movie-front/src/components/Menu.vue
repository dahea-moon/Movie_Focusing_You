<template>
    <Bubble id="page-wrap">
        <router-link to="/signup">
            <span v-show="!isLoggedIn">Sign Up</span>
        </router-link>
        <router-link to="/home">
            <span v-show="isLoggedIn">Home</span>
        </router-link>
        <router-link to="/mypage">
            <span v-show="isLoggedIn">My Page</span>
        </router-link>
        <router-link to="/all">
            <span v-show="isLoggedIn">전체 영화보기</span>
        </router-link>
    </Bubble>
</template>

<script>
import { Bubble } from 'vue-burger-menu'
import { mapGetters } from 'vuex';

export default {
    name: "menu",
    components: {
        Bubble
    },
    computed: {
    ...mapGetters(['isLoggedIn'])
    }
}
</script>

<style>

</style>