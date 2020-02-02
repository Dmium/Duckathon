<template>
  <div>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <b-button size="lg" variant="primary" :to="{ name: 'nuke'}">NUKE</b-button>
    <br/>
    <br/>
    <b-button size="lg" variant="primary" :to="{ name: 'reversenuke'}">REVERSE-NUKE</b-button>
    <br/>
    <br/>
    <b-button size="lg" variant="primary" :to="{ name: 'recentsplaylist'}">PLAYLIST OF RECENT TRACKS</b-button>
    <br/>
    <br/>
    <b-button size="lg" variant="primary" :to="{ name: 'playlistchain'}">Title Chain</b-button>
  </div>
</template>

<script>

export default {
  name: 'tools',
  components: {
  },
  data() {
    return {
      allPlaylists: [],
      filteredPlaylists: [],
    }
  },
  mounted() {
  },
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

.search {
  width: 60%;
  margin-left: 20%;
  margin-top: 5%;
}
</style>
