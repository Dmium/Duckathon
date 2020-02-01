<template>
    <b-media tag="li">
        <template v-slot:aside>
            <b-img :src="image" width="64" alt="placeholder"></b-img>
        </template>

        <h5 class="mt-0">{{ this.title }}</h5>
        <div v-for="artist in artists"  :key="artist.id">
            {{ artist.name }}, 
        </div>
    </b-media>
</template>

<script>

export default {
  name: 'track-preview',
  props: {
      id: String,
      title: String,
      artists: Array,
      image: String
  }
}
</script>

