<template>
  <div class="playlists">
    <h1>Create Playlist</h1>
    <b-form class="new-playlist-form" @submit="onSubmit">
      <b-form-group>
        <b-form-input
          id="new-playlist-input"
          v-model="playlist.name"
          required
          placeholder="Enter new playlist name"
          size="lg"
        ></b-form-input>
      </b-form-group>
      <br/>
      <PlaylistPreview class="playlist" :title="playlist.name" image="https://image.flaticon.com/icons/svg/2284/2284983.svg" id="new"/>

      <b-button type="submit" variant="primary" size="lg">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
import PlaylistPreview from '../components/PlaylistPreview.vue';
export default {
  name: 'newplaylist',
  components: {
      PlaylistPreview
  },
  data() {
    return {
      playlist: {
          name: "Asd",
      },
    }
  },
  methods: {
    onSubmit() {
        this.$http.post('playlists/create', this.playlist)
        this.$router.push({ name: "playlists"})
    }
  }
}
</script>

<style>
.new-playlist-form {
  width: 60%;
  margin-left: 20%;
  margin-top: 5%;
}
</style>
