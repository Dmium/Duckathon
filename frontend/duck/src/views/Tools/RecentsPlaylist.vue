<template>
  <div>

    <h1>Create a playlist of your recently listened to songs</h1>

    <br/>
    <br/>

    <b-button size="lg" variant="primary" v-on:click="createrecentsplaylist">Create Playlist</b-button>

  </div>
</template>

<script>

export default {
  name: 'recentsplaylist',
  components: {
  },
  data() {
    return {
      allTracks: [],
      songname: "",
    }
  },
  methods: {
    mounted() {
    },
    createrecentsplaylist() {
        this.$http.post('playlists/create/recent_tracks')
        this.$router.push({ name: "tools"})
    },
  },
}
</script>

<style>

.playlist-table {
    width: 90%;
    margin-left: 5%;
    margin-top: 5%;
    text-align: left;
    height: 60vh;
}

.playlist {
    margin: 1rem 0 1rem 0;
}

.album-icon {
  width: 15%;
}

.playlist-songs {
  height: 100vh;
}
</style>
