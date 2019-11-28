<template>
    <div>
        <h1 class="ui header">
            SIGN UP
        </h1>
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