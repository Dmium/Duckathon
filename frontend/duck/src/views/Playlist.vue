<template>
  <div class="playlists">
    <h1><b-img :src="this.playlist.images[0].url" width="64" alt="placeholder"></b-img>  {{playlist.name}}</h1>
    <ul class="playlist-container">
        <div v-for="track in tracks.items" :key="track.id">
            <TrackPreview class="playlist" :title="track.track.name" :artists="track.track.artists" :image="track.track.album.images[0].url" :id="track.track.id"/>
        </div>
    </ul>
  </div>
</template>

<script>
import TrackPreview from '../components/TrackPreview.vue';

export default {
  name: 'playlist',
  components: {
      TrackPreview
  },
  data() {
    return {
      playlist: {},
      tracks: [],
      id: ""
    }
  },
  created() {
    this.id = this.$route.params.id
    this.$http.get('playlist/' + this.id)
      .then(response => {
        // JSON responses are automatically parsed.
        this.playlist = response.data
        this.tracks = this.playlist.tracks
        console.log(this.tracks)
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
