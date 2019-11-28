<template>
  <div>
      <h2 class="ui center aligned icon header">
        <i class="circular users icon"></i>
            {{ getUserDetail.username }}
      </h2>
      <br>
      <dl class="row">
            <dt class="col-sm-6">1번째 선호 키워드</dt>
            <dd class="col-sm-6">{{ getUserDetail.k1_content }}</dd>

            <dt class="col-sm-6">2번째 선호 키워드</dt>
            <dd class="col-sm-6">{{ getUserDetail.k2_content }}</dd>
            
            <dt class="col-sm-6">1번째 선호 장르</dt>
            <dd class="col-sm-6">{{ getUserDetail.g1_name }}</dd>
            
            <dt class="col-sm-6">2번째 선호 장르</dt>
            <dd class="col-sm-6">{{ getUserDetail.g2_name }}</dd>
            
            <dt class="col-sm-6">보고 싶은 영화 목록</dt>
            <dd class="col-sm-6" v-for="wish in getUserDetail.wishlist" :key="wish.id">{{ wish }}</dd>
            <dt class="col-sm-6">내가 봤던 영화 목록</dt>
            <dd class="col-sm-6" v-for="watched in getUserDetail.watchedlist" :key="watched.id">{{ watched }}</dd>
        </dl>
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