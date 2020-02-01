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

      <b-button type="submit" variant="primary" size="lg">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: 'newplaylist',
  data() {
    return {
      playlist: {
          name: null,
      },
    }
  },
  methods: {
    onSubmit() {
      // handle making new playlist
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
