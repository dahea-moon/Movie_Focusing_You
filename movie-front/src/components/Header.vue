<template>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      
      <sweet-modal icon="success" ref="modal" title="New Modal">
        Success!
        <sweet-button slot="button">That's fine!</sweet-button>
      </sweet-modal>
      <button @click="open">Login</button>
     
      <span>
        <a @click.prevent="" href="">LogOut</a>
      </span>
    </div>
</template>

<script>
// import login from '@/components/Login.vue'
import { SweetModal } from 'sweet-modal-vue'

export default {
  name: "header",
  components: {
    SweetModal,
  },
  methods: {
    open: function () {
      this.$refs.modal.open()
    }
  }

}
</script>

<style>

</style>