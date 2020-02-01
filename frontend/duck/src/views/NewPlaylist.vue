<template>
  <div class="playlists">
    <h1>Create Playlist</h1>
    <b-form-input v-model="this.playlist.name" placeholder="Enter playlist name"></b-form-input>
    {{this.playlist.name}}
  </div>
</template>

<script>
// import PlaylistPreview from '../components/PlaylistPreview.vue';

export default {
  name: 'newplaylist',
  components: {
    //   PlaylistPreview
  },
  data() {
    return {
      playlist: {
          "name": "asd"
      },
    }
  },
  created() {

    // this.$http.get('playlists')
    //   .then(response => {
    //     // JSON responses are automatically parsed.
    //     this.playlists = response.data.items
    //     console.log(this.playlists[0]['images'][2]['url'])
    //   })
    //   .catch(e => {
    //     this.errors.push(e)
    //   })
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
</style>
