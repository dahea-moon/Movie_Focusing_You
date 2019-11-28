<template>
  <div class="ui text container">
    <h1 class="ui header">
      Movie Focusing You
    </h1>
    <h2>We will recommend movies for you</h2>
    <br>
    <div class="ui huge button black">
      <router-link to="/signup">Sign Up</router-link>
    </div>
    <br>
    <hr/>
    <div class="ui huge button black">
      <span v-show="!isLoggedIn" @click="open">Login</span>
    </div>
    <sweet-modal ref="modal" title="Welcome!">
      <Login/>
    </sweet-modal>
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