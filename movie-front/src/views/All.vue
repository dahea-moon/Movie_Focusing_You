<template>
    <div>
        <div>
            <b-modal id="modal-center" centered :title="getMovie.title">
                <p class="my-4">{{ getMovie }}</p>
                <img :src="getMovie.poster" :alt="getMovie.title">
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
        <div v-for="movie in getMovielist" :key="movie.id">
            <img :src="movie.poster" :alt="movie.title">
            <b-button v-b-modal.modal-center @click="pushtoMovie(movie)">{{ movie.title }}</b-button>
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