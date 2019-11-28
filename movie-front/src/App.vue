<template>
  <div id="app">
    <Header></Header>
    <Menu></Menu>
    <router-view/>
  </div>
</template>

<script>
import Menu from '@/components/Menu.vue'
import Header from '@/components/Header.vue'

export default {
  name: 'app',
  components: {
    Header,
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
