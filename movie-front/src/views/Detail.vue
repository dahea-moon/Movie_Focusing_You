<template>
    <div>
        <SweetModal ref="modal">
        끝
        </SweetModal>
        <span @click="open">평가하기</span>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { SweetModal } from 'sweet-modal-vue'

export default {
    name: 'detail',
    components: {
        SweetModal,
    },
    methods: {
        ...mapGetters(['getMovie']),
        open () {
            return this.$refs.modal.open()
        },
        close () {
            return this.$refs.modal.close()
        }
    },
    created () {
        const movieid = this.$store.getters('getMovieid')
        this.$store.dispatch('상세보기', movieid)
    }
}
</script>

<style>

</style>