<template>
    <div>
        회원가입
        <signupform/>
    </div>
</template>

<script>
import signupform from '@/components/SignupForm.vue'

export default {
    name: 'signup',
    components: {
        signupform
    }
}
</script>

<style>

</style>