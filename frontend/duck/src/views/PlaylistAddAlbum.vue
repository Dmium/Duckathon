<template>
  <div>
    <div class="back-link">
      <router-link :to="{ name: 'playlists' }">Back to {{ name }}</router-link>
    </div>
    <h1>Search for an artist</h1>
    <b-form class="new-playlist-form" @submit="onSubmit">
      <b-form-group>
        <vue-bootstrap-typeahead size="lg" placeholder="Search for an artist..." :data="allArtists" v-model="artistname" :maxMatches="9"></vue-bootstrap-typeahead>
      </b-form-group>
      <b-button type="submit" variant="primary" size="lg">Submit</b-button>
    </b-form>
    <div class="artist-list">
      <b-row cols="3">
        <b-col v-for="artist in allArtists" :key="artist.id">
          <ArtistPreview class="playlist" :name="artist.name" :image="artist.images[0]" :id="artist.id" :albums="true" :playlist="id"/>
        </b-col>
      </b-row>
    </div>

  </div>
</template>

<script>

import ArtistPreview from '../components/ArtistPreview.vue';
import _ from 'underscore'

export default {
  name: 'playlistaddalbum',
  components: {
      ArtistPreview
  },
  props: {
      id: String,
      name: String,
  },
  data() {
    return {
      allArtists: [],
      artistname: "",
    }
  },
    mounted() {
        this.id = this.$route.params.id
    },
  methods: {
    async getArtists(query) {
      this.$http.get('search/artist/' + query)
            .then(response => {
                this.allArtists = response.data.artists.items
            })
            .catch(e => {
                this.errors.push(e)
            })
    },
    async onSubmit() {
      await this.getArtists(); 
    }
  },
  watch: {
    artistname: _.debounce(function(artist) { this.getArtists(artist) }, 500)
  }
}
</script>

<style>
.artist-list {
  width: 80%;
  margin-left: 10%;
}
</style>