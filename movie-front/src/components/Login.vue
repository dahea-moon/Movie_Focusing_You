<template>
  <form class="ui large form">
    <div class="field">
      <div class="ui fluid left icon input">
        <i class="user icon"></i>
        <input name="User" v-model="credentials.username" placeholder="Username">
      </div>
    </div>

    <div class="field">
      <div class="ui fluid left icon input">
        <i class="lock icon"></i>
        <input name="password" type="password" v-model="credentials.password" placeholder="Password">
      </div>
    </div>
    <div class="ui fluid large black submit button" @click="$router.push('/home')" @click.prevent="login(credentials)">로그인</div>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'login',
  data() {
    return {
      credentials: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
      ...mapActions(['login'])
  },
  computed: {
      ...mapGetters(['getErrors'])
  }
};
</script>