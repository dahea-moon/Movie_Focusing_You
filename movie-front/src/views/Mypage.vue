<template>
  <div>
      my page
      {{ getUserDetail }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: "mypage",
    computed: {
        ...mapGetters(['getUserDetail'])
    },
    created () {
        this.$store.dispatch('detail')
    }
}
</script>

<style>

</style>