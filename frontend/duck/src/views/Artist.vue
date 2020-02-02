<template>
  <div>
    <h1>Albums</h1>
    <div v-for="album in allAlbums" :key="album.id">
        <AlbumPreview :name="album.name" :image="album.images[0]" :id="album.id" :addtoplaylist="true" :playlist="playlistid"/>
    </div>
  </div>
</template>

<script>

import AlbumPreview from '../components/AlbumPreview.vue';
export default {
  name: 'artist',
  components: {
      AlbumPreview
  },
  data() {
    return {
      allAlbums: [],
      artistid: "",
      playlistid: ""
    }
  },
  mounted() {
    this.playlistid = this.$route.params.playlistid
    this.artistid = this.$route.params.artistid
    this.$http.get('artist/' + this.artistid + '/albums')
    .then(response => {
        this.allAlbums = response.data.albums
    })
    .catch(e => {
        this.errors.push(e)
    })
  },
  methods: {
  }
}
</script>

<style>
</style>
