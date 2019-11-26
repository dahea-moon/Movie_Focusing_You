<template>
    <div>
        <div v-if="getErrors.length">
            <p>아래의 오류를 해결해 주세요</p>
            <ul>
                <li v-for="(error, idx) in getErrors" :key="idx">
                    {{ error }}
                </li>
            </ul>
        </div>
        <div>
            <label for="username">아이디</label>
            <input type="text" v-model="userInfo.username" name="username" id="username" placeholder="아이디를 입력해주세요">
            <label for="pwd">비밀번호</label>
            <input type="password"  v-model="userInfo.password" name="pwd">
            <label for="pwd2">비밀번호 재확인</label>
            <input type="password"  v-model="userInfo.passwordconfirm" name="pwd2">
            <label for="Email">이메일</label>
            <input type="email" name="Email" id="Email" v-model="userInfo.email">
            <label for="genre1">가장 선호하는 장르</label>
            <select name="genre1" id="" v-model="userInfo.genre1">
                <option value="1">드라마</option>
                <option value="2">뮤직</option>
                <option value="3">전기</option>
                <option value="4">미스터리</option>
                <option value="5">SF</option>
                <option value="6">코미디</option>
                <option value="7">액션</option>
                <option value="8">범죄</option>
                <option value="9">어드벤처</option>
                <option value="10">가족</option>
                <option value="11">멜로드라마</option>
                <option value="12">공포</option>
                <option value="13">스릴러</option>
                <option value="14">전쟁</option>
                <option value="15">판타지</option>                                                                    
            </select>
            <label for="genre2"></label>
                <select name="genre2" id=""  v-model="userInfo.genre2">
                <option value="1">드라마</option>
                <option value="2">뮤직</option>
                <option value="3">전기</option>
                <option value="4">미스터리</option>
                <option value="5">SF</option>
                <option value="6">코미디</option>
                <option value="7">액션</option>
                <option value="8">범죄</option>
                <option value="9">어드벤처</option>
                <option value="10">가족</option>
                <option value="11">멜로드라마</option>
                <option value="12">공포</option>
                <option value="13">스릴러</option>
                <option value="14">전쟁</option>
                <option value="15">판타지</option>                                                                    
                </select>
            <button type="submit" @click.prevent="signup(userInfo)">회원가입</button>      
        </div>
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