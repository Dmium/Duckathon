<template>
  <div class="playlists">
    <h1>Your Playlists</h1>
    <div class="new">
      <router-link :to="{ name: 'newplaylist'}">
        <b-button size="lg" variant="primary">New Playlist</b-button>
      </router-link>
    </div>
    <div class="search">
      <vue-bootstrap-typeahead placeholder="Search for a playlist..." size="lg" :data="filteredPlaylists" :serializer="p => p.name" :minMatchingChars="1" @hit="goToPlaylist($event)"/>
    </div>
    <div class="album-list">
      <b-row cols="3">
        <b-col v-for="playlist in filteredPlaylists" :key="playlist.id">
          <PlaylistPreview v-if="playlist.images[0] != null" class="playlist" :title="playlist.name" :description="playlist.description" :image="playlist.images[0].url" :id="playlist.id"/>
          <PlaylistPreview v-if="playlist.images[0] == null" class="playlist" :title="playlist.name" :description="playlist.description" image="https://image.flaticon.com/icons/svg/2284/2284983.svg" :id="playlist.id"/>
        </b-col>
      </b-row>
    </div>
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
        console.log(e);
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
  width: 80%;
  margin-left: 10%;
  margin-top: 5%;
}

.album-icon-lg {
  width: 70%;
}

.album-list {
  width: 80%;
  margin-left: 10%;
}
</style>
