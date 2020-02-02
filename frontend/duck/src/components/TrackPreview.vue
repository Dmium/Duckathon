<template>
    <b-media tag="li">
        <template v-slot:aside>
            <b-img :src="image" width="64" alt="placeholder"></b-img>
        </template>

        <h5 class="mt-0">{{ this.title }}</h5>
        <div v-for="artist in artists"  :key="artist.id">
            {{ artist.name }}
        </div>
        <b-button v-if="nuke == true" size="lg" variant="primary" v-on:click="nukesong">NUKE</b-button>
    </b-media>
</template>

<script>

export default {
  name: 'track-preview',
  props: {
      id: String,
      title: String,
      artists: Array,
      image: String,
      nuke: Boolean
  },
  methods: {
    nukesong() {
        this.$http.post('nuke', {"id": this.id})
        this.$router.push({ name: "tools"})
    },
  },
}
</script>

