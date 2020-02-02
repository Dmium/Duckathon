<template>
  <div>

    <h1>Search for a song to nuke</h1>
    <b-form class="new-playlist-form" @submit="onSubmit">
      <b-form-group>
        <b-form-input
          id="new-playlist-input"
          v-model="songname"
          required
          placeholder="Enter a song name"
          size="lg"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary" size="lg">Submit</b-button>
    </b-form>

    <br/>
    <br/>
    <div v-for="track in allTracks" :key="track.id">
        <TrackPreview class="playlist" :title="track.name" :artists="track.artists" :image="track.album.images[0].url" :id="track.id" :nuke="true"/>
    </div>

  </div>
</template>

<script>
import TrackPreview from '../../components/TrackPreview.vue';

export default {
  name: 'nuke',
  components: {
      TrackPreview
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
    onSubmit() {
        this.$http.get('search/track/' + this.songname)
            .then(response => {
                this.allTracks = response.data.tracks.items
            })
            .catch(e => {
                this.errors.push(e)
            })
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
