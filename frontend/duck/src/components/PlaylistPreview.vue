<template>
    <b-media tag="li">
        <template v-slot:aside>
            <b-img :src="image" width="64" alt="placeholder"></b-img>
        </template>

        <h5 class="mt-0">{{ this.title }}</h5>
        <p v-if="this.id !== 'new'">
            {{ this.description }}
            <router-link :to="{ name: 'playlist', params: {id: this.id } }">Edit</router-link>
        </p>
    </b-media>
</template>

<script>

export default {
  name: 'playlist-preview',
  props: {
      id: String,
      title: String,
      description: String,
      image: String
  }
}
</script>

<style>
.playlist-container {
    width: 40%;
    margin-left: 30%;
    margin-top: 5%;
    text-align: left;
}

.playlist {
    margin: 1rem 0 1rem 0;
}
</script>
