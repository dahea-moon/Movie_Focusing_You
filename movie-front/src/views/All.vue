<template>
    <div>
        <div>
            <b-modal id="modal-center" centered :title="getMovie.title">
                <b-img center :src="getMovie.poster" :alt="getMovie.title"></b-img>
                <p class="my-4">감독: {{ getMovie.director }}</p>
                <p class="my-4">배우: {{ getMovie.actors }}</p>
                <p class="my-4">줄거리: {{ getMovie.plot }}</p>
                <template v-slot:modal-footer="{ ok, cancel }">
                    <router-link to="/detail">
                        <b-button size="sm" variant="success">
                            상세보기
                        </b-button>
                    </router-link>
                    <b-button size="sm" variant="danger" @click="cancel()">
                        닫기
                    </b-button>
                </template>
            </b-modal>
        </div>
        <div class="ui link four cards">
            <div class="card" v-for="movie in getMovielist" :key="movie.id">
                <div class="image">
                    <img :src="movie.poster" :alt="movie.title">
                </div>
                <div class="content">
                    <div class="header">
                        <b-button v-b-modal.modal-center @click="pushtoMovie(movie)">{{ movie.title }}</b-button>
                    </div>
                    <div class="meta">
                        <a>{{ movie.titleEng }}</a>
                    </div>
                    <div class="description">
                        <a>{{ movie.descriptions }}</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
// import Modal from '@/components/Modal.vue'


export default {
    name: 'all',
    components: {
        // Modal
    },
    methods: {
        ...mapActions(['allMovie', 'pushtoMovie']),
    },
    computed: {
        ...mapGetters(['getMovielist', 'getMovie'])
    },
    created () {
        this.allMovie()
    }
}
</script>

<style>

</style>