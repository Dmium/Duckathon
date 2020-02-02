<template>
  <div class="playlists">
    <h1>Create Playlist</h1>
    <b-form class="new-playlist-form" @submit="onSubmit">
      <b-form-group>
        <b-form-input
          id="new-playlist-input"
          v-model="playlist.starter"
          required
          size="lg"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary" size="lg">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: 'playlistchain',
  components: {
  },
  data() {
    return {
      playlist: {
          starter: "Enter starting word"
      },
    }
  },
  methods: {
    onSubmit() {
        this.$http.get('playlists/title_chain/' + this.playlist.starter)
        this.$router.push({ name: "tools"});
    },
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
