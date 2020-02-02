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
    <b-button size="lg" variant="primary" :to="{ name: 'playlistaddalbum', params: {id: playlist.id, name: playlist.name } }">Add Albums</b-button>
    <b-button size="lg" variant="primary" :to="{ name: 'removebykeyword', params: {id: this.id } }">Remove by Keyword</b-button>
    <div class="playlist-table">
      <TrackPreview v-for="track in tracks.items" v-bind:key="track.id" :id="track.id" :title="track.title"></TrackPreview>
    </div>
  </div>
</template>

<script>
import TrackPreview from '../components/TrackPreview.vue';

export default {
  name: 'playlist',
  components: {
    TrackPreview
  },
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
    padding-bottom: 0;
}

.playlist {
    margin: 1rem 0 1rem 0;
}

.album-icon {
  width: 15%;
}

.back-link {
  text-align: left;
  margin-left: 5%;
  margin-top: 2%;
}
</style>
