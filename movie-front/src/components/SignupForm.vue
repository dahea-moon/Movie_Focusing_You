<template>
    <div class="ui container">
        <div v-if="getErrors.length">
            <p>아래의 오류를 해결해 주세요</p>
            <li v-for="(error, idx) in getErrors" :key="idx">
                {{ error }}
            </li>
        </div>
        <b-form>
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

        <b-form-group id="input-group-4" label="Your Password:" label-for="input-4">
            <b-form-input
            id="input-4"
            type="password"
            v-model="userInfo.password"
            required
            placeholder="Enter Password"
            ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-7" label="Password Confirmation:" label-for="input-4">
            <b-form-input
            type="password"
            id="input-7"
            v-model="userInfo.passwordconfirm"
            required
            placeholder="Enter Password"
            ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="First Favorite Genre:" label-for="input-3">
            <b-form-select
            id="input-3"
            v-model="userInfo.genre1"
            required
            >
            <option v-for="genre in genres" :key="genre.id" :value="genre.id">{{genre.value}}</option>
            </b-form-select>
        </b-form-group>

        <b-form-group id="input-group-5" label="Second Favorite Genre:" label-for="input-5">
            <b-form-select
            id="input-5"
            v-model="userInfo.genre2"
            required
            >
            <option v-for="genre in genres" :key="genre.id" :value="genre.id">{{genre.value}}</option>
            </b-form-select>
        </b-form-group>
        <b-button type="submit" variant="primary" @click.prevent="signup(userInfo)">Submit</b-button>
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
            genres: [{id:1, value:'드라마'}, {id:2, value:'뮤직'}, {id:3, value:'전기'}, {id:4, value:'미스터리'}, {id:5, value:'SF'}, {id:6, value:'코미디'}, {id:7, value:'액션'}, {id:8, value:'범죄'}, {id:9, value:'어드벤처'}, {id:10, value:'가족'}, {id:11, value:'멜로드라마'}, {id:12, value:'공포'}, {id:13, value:'스릴러'}, {id:14, value:'전쟁'}, {id:15, value:'판타지'}]
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