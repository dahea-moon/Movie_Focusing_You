<template>
  <div class="c-modalLogin">
    <div>
      <label for="name">User</label>
      <input name="User">
    </div>

    <div>
      <label for ="password">Password</label>
      <input name="password" type="password">
    </div>

    <button class="c-modalLogin__cancel" @click="hideModal">Cancel</button>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
  name: 'ModalLogin',
  methods: {
    ...mapMutations([
      'hideModal',
    ]),
  },
};
</script>