<template>
  <div class="artist">
        <img class="album-icon-lg" v-if="image != null" :src="image.url"/>
        <img v-else class="album-icon-lg" src="https://image.flaticon.com/icons/svg/2284/2284983.svg"/>
        <h5>{{ name }}</h5>
        <b-button-group>
          <router-link tag="b-button" :to="{ name: 'artist', params: {playlistid: playlist, artistid: id} }">
            View Albums
          </router-link>
          <b-button @click="addAlbums()">Add all albums to playlist</b-button>
        </b-button-group>
  </div>
</template>

<script>

export default {
  name: 'artist-preview',
  props: {
      id: String,
      name: String,
      image: Object,
      albums: Boolean,
      playlist: String,
  },
  data() {
    return {
      playlistid: "",
      artistid: "",
      allArtists: [],
      artistname: "",
    }
  },
}
</script>

<style>
.album-icon-lg {
  width: 70%;
}
</style>

