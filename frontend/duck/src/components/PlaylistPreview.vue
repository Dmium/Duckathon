<template>
    <b-media tag="li">
        <template v-slot:aside>
            <b-img :src="image" width="64" alt="placeholder"></b-img>
        </template>

        <h5 class="mt-0">{{ this.title }}</h5>
        <p>
            {{ this.description }}
            <router-link :to="{ name: 'playlist', params: {id: this.id } }">Edit</router-link>
        </p>
    </b-media>
</template>

<script>

export default {
  name: 'playlist-preview',
  props: {
      id: Number,
      title: String,
      description: String,
      image: String
  }
}
</script>

