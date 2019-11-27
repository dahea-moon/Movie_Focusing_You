<template>
    <div>
        <div v-for="(movie, idx) in getMovielist" :key="movie.id">
            <SweetModal :ref="modal" :title="movie.title">
                {{ idx }}
                {{ movie.title }}
                <!-- <sweet-button @click="">상세보기</sweet-button> -->
                <!-- 상세보기를 누르면 영화의 아이디를 state의 movieid로 mutate 한다 그걸 detail 페이지에서 받게한다 -->
                <sweet-button @click="close">취소</sweet-button>
            </SweetModal>
            <img :src="movie.poster" :alt="movie.title">
            {{movie.id}}
            <span @click="open(idx)"> {{ movie.title }} </span>
        </div>
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
        open (idx) {
            // console.log(this.$refs[`modal-${pk}`][0])
            // console.log(pk)
            // return this.$refs[`modal-${pk}`].open()
            console.log(this.$refs.modal)
            return this.$refs.modal[idx].open()
        },
        close () {
            return this.$refs.modal.close()
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