<template>
  <div class="playlists">
    <h1>Your Playlists</h1>
    <div class="new">
      <router-link :to="{ name: 'newplaylist'}">
        <b-button size="lg" variant="primary">New Playlist</b-button>
      </router-link>
    </div>
    <div class="search">
      <vue-bootstrap-typeahead placeholder="Search for a playlist..." size="lg" v-model="selected" :data="filteredPlaylists" :serializer="p => p.name" :minMatchingChars="1" @hit="goToPlaylist($event)"/>
    </div>
    <ul class="playlist-container">
        <div v-for="playlist in filteredPlaylists" :key="playlist.id">
            <PlaylistPreview class="playlist" :title="playlist.name" :description="playlist.description" :image="playlist.images[0].url" :id="playlist.id"/>
            <PlaylistPreview v-if="playlist.images[0] == null" class="playlist" :title="playlist.name" :description="playlist.description" image="https://image.flaticon.com/icons/svg/2284/2284983.svg" :id="playlist.id"/>
        </div>
    </ul>
  </div>
</template>

<script>
import PlaylistPreview from '../components/PlaylistPreview.vue';

export default {
  name: 'playlists',
  components: {
      PlaylistPreview
  },
  data() {
    return {
      allPlaylists: [],
      filteredPlaylists: [],
    }
  },
  mounted() {

    this.$http.get('playlists')
      .then(response => {
        this.allPlaylists = response.data.items
        this.filteredPlaylists = response.data.items
      })
      .catch(e => {
        this.errors.push(e)
      })
  },
  methods: {
    goToPlaylist(selected) {
      this.$router.push({ name: 'playlist', params: {id: selected.id } });
    }
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
