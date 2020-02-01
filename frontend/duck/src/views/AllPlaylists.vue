<template>
  <div class="playlists">
    <h1>Your Playlists</h1>
    <ul class="playlist-container">
        <PlaylistPreview title="Sample Playlist" description="A description" image="https://image.flaticon.com/icons/svg/1753/1753344.svg"/>
        <PlaylistPreview title="Another sample playlist" description="Now these can be used in list rendering" image="https://image.flaticon.com/icons/svg/1753/1753344.svg"/>
    </ul>
  </div>
</template>

<script>
import PlaylistPreview from '../components/PlaylistPreview.vue';

export default {
  name: 'playlists',
  components: {
      PlaylistPreview
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
</style>
