<template>
  <div class="playlist-songs">
    <div class="back-link">
      <router-link :to="{ name: 'playlists' }">Back to all playlists</router-link>
    </div>
    <h1>
    <b-img v-if="playlist.images[0] != null" :src="this.playlist.images[0].url" width="64" alt="placeholder"></b-img>
    <b-img v-if="playlist.images[0] == null" src="https://image.flaticon.com/icons/svg/2284/2284983.svg" width="64" alt="placeholder"></b-img>    
    {{playlist.name}}</h1>
    <br/>
    <b-button size="lg" variant="primary" :to="{ name: 'playlistaddalbum', params: {id: this.id } }">Add Albums</b-button>
    <div class="playlist-table">
      <b-table-simple hover small caption-top responsive sticky-header borderless text-white> 
        <b-thead head-variant="dark">
          <b-tr>
            <b-th colspan="2">Song</b-th>
            <b-th>Artist</b-th>
            <b-th>Album</b-th>
            <b-th>Actions</b-th>
          </b-tr>
        </b-thead>
        <b-tbody class="text-white">
          <b-tr v-for="track in tracks.items" v-bind:key="track.id">
            <b-td>
              <img v-if="track.track.album.images[0] !=  null" class="album-icon" :src="track.track.album.images[0].url"/>
              <img v-else class="album-icon" src="https://image.flaticon.com/icons/svg/2284/2284983.svg"/>
            </b-td>
            <b-th>{{ track.track.name }}</b-th>
            <b-td>{{ formatArtists(track.track.artists)}}</b-td>
            <b-td>{{ track.track.album.name }}</b-td>
            <b-td>Delete/nuke/idk what else</b-td>
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
  methods: {
    formatArtists(artists) {
      if(artists.length === 1) return artists[0].name;
      var response = '';
      artists.forEach(artist => response += artist.name + ", ");
      return response;
    }
  },
    mounted() {
        this.id = this.$route.params.id
        this.$http.get('playlist/' + this.id)
        .then(response => {
            // JSON responses are automatically parsed.
            this.playlist = response.data
            this.tracks = this.playlist.tracks
        })
        .catch(e => {
            this.errors.push(e)
        })
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

.back-link {
  text-align: left;
  margin-left: 5%;
  margin-top: 2%;
}
</style>
