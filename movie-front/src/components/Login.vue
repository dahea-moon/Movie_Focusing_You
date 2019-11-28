<template>
  <div>
    <div>
      <label for="name">User</label>
      <input name="User" v-model="credentials.username">
    </div>

    <div>
      <label for ="password">Password</label>
      <input name="password" type="password" v-model="credentials.password">
    </div>
    <button type="submit" @click="$router.go(-1)" @click.prevent="login(credentials)">로그인</button>
  </div>
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