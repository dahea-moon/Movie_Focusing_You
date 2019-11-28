<template>
    <div id="nav">
      <span v-show="isLoggedIn">
        <a @click.prevent="logout" href="">LogOut</a>
      </span>

      <span v-show="isLoggedIn">
        <a href="">{{ getUsername }}</a>
      </span>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: "header",
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