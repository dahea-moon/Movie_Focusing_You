<template>
    <div>
        <div v-for="movie in getMovielist" :key="movie.id">
            <SweetModal :ref="modal">
                음
                <sweet-button @click="close">취소</sweet-button>
            </SweetModal>
            <img :src="movie.poster" :alt="movie.title">
            {{movie.id}}
            <span @click="open()"> {{ movie.title }} </span>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { SweetModal } from 'sweet-modal-vue'
// import Modal from '@/components/Modal.vue'

export default {
    name: 'all',
    components: {
        SweetModal,
        // Modal
    },
    methods: {
        ...mapActions(['allMovie']),
    },
    computed: {
        ...mapGetters(['getMovielist'])
    },
    created () {
        this.allMovie()
    }
}
</script>

<style>

</style>