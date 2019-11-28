<template>
    <div class="ui container">
        <div v-if="getErrors.length">
            <p>아래의 오류를 해결해 주세요</p>
            <li v-for="(error, idx) in getErrors" :key="idx">
                {{ error }}
            </li>
        </div>
        <b-form @submit="signup(userInfo)">
        <b-form-group
            id="input-group-1"
            label="Email address:"
            label-for="input-1"
            description="We'll never share your email with anyone else."
        >
            <b-form-input
            id="input-1"
            v-model="userInfo.email"
            type="email"
            required
            placeholder="Enter email"
            ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
            <b-form-input
            id="input-2"
            v-model="userInfo.username"
            required
            placeholder="Enter ID"
            ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-4" label="Your Passwird:" label-for="input-4">
            <b-form-input
            id="input-4"
            v-model="userInfo.password"
            required
            placeholder="Enter Password"
            ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="First Favorite Genre:" label-for="input-3">
            <b-form-select
            id="input-3"
            v-model="userInfo.genre1"
            :options="genres"
            required
            ></b-form-select>
        </b-form-group>

        <b-form-group id="input-group-5" label="Second Favorite Genre:" label-for="input-5">
            <b-form-select
            id="input-5"
            v-model="userInfo.genre2"
            :options="genres"
            required
            ></b-form-select>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    name: 'signupform',
    data() {
        return {
            userInfo: {
                username: '',
                password: '',
                passwordconfirm: '',
                email: '',
                genre1: 0,
                genre2: 0
            },
            genres: ['드라마', '뮤직', '전기', '미스터리', 'SF', '코미디', '액션', '범죄', '어드벤처', '가족', '멜로드라마', '공포', '스릴러', '전쟁', '판타지']
        }
    },
    methods: {
        ...mapActions(['signup'])
    },
    computed: {
        ...mapGetters(['getErrors'])
    }
}

</script>

<style>

</style>