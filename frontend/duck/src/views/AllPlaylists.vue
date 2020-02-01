<template>
  <div class="playlists">
    <h1>Your Playlists</h1>
    <div class="new">
      <router-link :to="{ name: 'newplaylist'}">
        <b-button size="lg" variant="primary">New Playlist</b-button>
      </router-link>
    </div>
    <ul class="playlist-container">
        <div v-for="playlist in playlists" :key="playlist.id">
            <PlaylistPreview class="playlist" :title="playlist.name" :description="playlist.description" :image="playlist.images[0].url" :id="playlist.id"/>
        </div>
    </ul>
  </div>
</template>

<script>
import PlaylistPreview from '../components/PlaylistPreview.vue';

export default {
  name: 'playlists',
  components: {
      PlaylistPreview
  },
  data() {
    return {
      playlists: [],
    }
  },
  created() {

    this.$http.get('playlists')
      .then(response => {
        // JSON responses are automatically parsed.
        this.playlists = response.data.items
        console.log(this.playlists[0]['images'][2]['url'])
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

.new {
  text-align: right;
  margin-right: 5%;
}
</style>
