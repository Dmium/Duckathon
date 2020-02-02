<template>
  <div>
    <h1>Albums</h1>
    
    <br/>
    <b-button size="lg" variant="primary" v-on:click="loadalbums">Albums</b-button>
    <b-button size="lg" variant="primary" v-on:click="loadsingles">Singles</b-button>
    <b-button size="lg" variant="primary" v-on:click="loadappears_ons">Appears On</b-button>
    <b-button size="lg" variant="primary" v-on:click="loadcompilations">Compilations</b-button>
    <br/>
    <br/>
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
      allData: {},
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
        this.allData = response.data
    })
    .catch(e => {
        this.errors.push(e)
    })
  },
  methods: {
      loadalbums() {
        this.allAlbums = this.allData.albums
      },
      loadsingles() {
        this.allAlbums = this.allData.singles
      },
      loadappears_ons() {
        this.allAlbums = this.allData.appears_ons
      },
      loadcompilations() {
        this.allAlbums = this.allData.compilations
      }
  }
}
</script>

<style>
</style>
