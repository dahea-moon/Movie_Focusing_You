<template>
  <div id="app">
    <Usernav></Usernav>
    <Menu></Menu>
    <router-view/>
  </div>
</template>

<script>
import Menu from '@/components/Menu.vue'
import Usernav from '@/components/Usernav.vue'

export default {
  name: 'app',
  components: {
    Usernav,
    Menu
  },
  created () {
    this.$store.dispatch('initialLogin')
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
