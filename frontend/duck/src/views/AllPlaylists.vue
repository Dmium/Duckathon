<template>
  <div class="playlists">
    <h1>Your Playlists</h1>
    <ul class="playlist-container">
        <PlaylistPreview class="playlist" title="Sample Playlist" description="A description" image="https://image.flaticon.com/icons/svg/2284/2284983.svg"/>
        <PlaylistPreview class="playlist" title="Another sample playlist" description="Now these can be used in list rendering" image="https://image.flaticon.com/icons/svg/2284/2284983.svg"/>
    </ul>
  </div>
</template>

<script>
import PlaylistPreview from '../components/PlaylistPreview.vue';
import axios from 'axios';

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
    axios.get('http://localhost:8000/playlists')
    .then(response => {
      this.playlists = response.data;
    })
    .catch(e => {
      console.log(e);
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
