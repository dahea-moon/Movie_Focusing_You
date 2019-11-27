<template>
    <div>
        <ul v-for="(movie) in getMovielist" :key="movie.pk">
            <sweet-modal ref="modal" :title="movie.title">
                {{ movie.title }}
                <sweet-button @click="">상세보기</sweet-button>
                <sweet-button @click="close">취소</sweet-button>
            </sweet-modal>
            <img :src="movie.poster" :alt="movie.title">
            <span @click="open"> {{ movie.title }} </span>
        </ul>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { SweetModal } from 'sweet-modal-vue'

export default {
    name: 'movielist',
    components: {
        SweetModal,
    },
    methods: {
        open: function () {
            return this.$ref.modal.open()
        }.bind(this),
        close: function () {
            return this.$ref.modal.close()
        }
    },
    computed: {
        ...mapGetters(['getMovielist'])
    },
    created () {
        this.$store.dispatch('recommendation')
    }
}
</script>

<style>

</style>