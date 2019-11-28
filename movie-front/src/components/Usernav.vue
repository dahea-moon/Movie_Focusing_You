<template>
  <div v-show="isLoggedIn" class="ui container">
    <div class="ui two item menu">
      <a class="item" v-show="isLoggedIn">
        {{ getUsername }}
      </a>
      <a class="item" v-show="isLoggedIn" @click.prevent="logout">LogOut</a>
    </div>
    <br>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: "usernav",
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
    ...mapGetters(['isLoggedIn', 'getUsername'])
  }
}
</script>

<style>

</style>