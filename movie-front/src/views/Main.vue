<template>
  <div>
    <router-link to="/signup">Sign Up</router-link> |
      
    <sweet-modal ref="modal" title="로그인">
      <Login/>
      <sweet-button @click="close">취소</sweet-button>
    </sweet-modal>
    <span v-show="!isLoggedIn" @click="open">Login</span>
  </div>
</template>

<script>
import { SweetModal } from 'sweet-modal-vue'
import Login from '@/components/Login.vue'
import { mapGetters } from 'vuex'

export default {
    name: 'main',
    components: {
      SweetModal,
      Login,
    },
    methods: {
      open () {
        return this.$refs.modal.open()
      },
      close () {
        return this.$refs.modal.close()
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn'])
    }
    
}
</script>

<style>

</style>