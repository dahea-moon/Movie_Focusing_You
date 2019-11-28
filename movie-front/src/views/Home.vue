<template>
    <div class="ui container">
        <h2>Movies for You</h2>
        <MovieList></MovieList>
    </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
    name: 'home',
    components: {
        MovieList
    }
}
</script>

<style>

</style>