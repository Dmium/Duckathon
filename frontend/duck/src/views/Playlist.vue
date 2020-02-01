<template>
  <div class="playlists">
    <h1>{{playlist.name}}</h1>
    <ul class="playlist-container">
        <PlaylistPreview class="playlist" :title="this.playlist.name" :description="this.playlist.description" :image="this.playlist.images[0].url" :id="this.playlist.id"/>
    </ul>
  </div>
</template>

<script>
import PlaylistPreview from '../components/PlaylistPreview.vue';

export default {
  name: 'playlist',
  components: {
      PlaylistPreview
  },
  data() {
    return {
      playlist: {},
      id: ""
    }
  },
  created() {
    this.id = this.$route.params.id
    this.$http.get('playlists/' + this.id)
      .then(response => {
        // JSON responses are automatically parsed.
        this.playlist = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
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
