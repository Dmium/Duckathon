<template>
    <b-media tag="li">
        <template v-slot:aside>
            <b-img :src="image" width="64" alt="placeholder"></b-img>
        </template>

        <h5 class="mt-0">{{ this.title }}</h5>
        <p>
            {{ this.description }}
        </p>
    </b-media>
</template>

<script>

export default {
  name: 'playlist-preview',
  props: {
      title: String,
      description: String,
      image: String
  }
}
</script>

