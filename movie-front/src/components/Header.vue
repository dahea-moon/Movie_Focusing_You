<template>
    <div id="nav">
      <router-link to="/signup">Sign Up</router-link> |
      
      <sweet-modal ref="modal" title="로그인">
        <Login/>
        <sweet-button @click="close">취소</sweet-button>
      </sweet-modal>
      <span v-show="!isLoggedIn" @click="open">Login</span>
     
      <span v-show="isLoggedIn">
        <a @click.prevent="logout" href="">LogOut</a>
      </span>

      <span>
        <a href="">{{ getUserpk }}</a>
      </span>
    </div>
</template>

<script>
import Login from '@/components/Login.vue'
import { mapActions, mapGetters } from 'vuex'
import { SweetModal } from 'sweet-modal-vue'

export default {
  name: "header",
  components: {
    SweetModal,
    Login,
  },
  methods: {
    ...mapActions(['logout']),
    open () {
      return this.$refs.modal.open()
    },
    close () {
      return this.$refs.modal.close()
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'getUserpk'])
  }
}
</script>

<style>

</style>