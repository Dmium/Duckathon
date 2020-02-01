<template>
  <div class="playlist-songs">
    <h1><b-img :src="this.playlist.images[0].url" width="64" alt="placeholder"></b-img>  {{playlist.name}}</h1>
    <div class="playlist-table">
      <b-table-simple hover small caption-top responsive sticky-header borderless>
        <b-thead head-variant="dark">
          <b-tr>
            <b-th colspan="2">Song</b-th>
            <b-th>Artist</b-th>
            <b-th>Album</b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr v-for="track in tracks.items" v-bind:key="track.id">
            <b-td><img class="album-icon" :src="track.track.album.images[0].url"/></b-td>
            <b-th>{{ track.track.name }}</b-th>
            <b-td>{{ formatArtists(track.track.artists)}}</b-td>
            <b-td>{{ track.track.album.name }}</b-td>
          </b-tr>
        </b-tbody>
      </b-table-simple>
    </div>
  </div>
</template>

<script>

export default {
  name: 'playlist',
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
  },
  methods: {
    formatArtists(artists) {
      if(artists.length === 1) return artists[0].name;
      var response = '';
      artists.forEach(artist => response += artist.name + ", ");
      return response;
    }
  }
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
