<template>
  <div>

    <h1>Search for an artist</h1>
    <b-form class="new-playlist-form" @submit="onSubmit">
      <b-form-group>
        <vue-bootstrap-typeahead size="lg" placeholder="Search for an artist..." :data="allArtists" v-model="artistname"></vue-bootstrap-typeahead>
      </b-form-group>
      <b-button type="submit" variant="primary" size="lg">Submit</b-button>
    </b-form>
    <div v-for="artist in allArtists" :key="artist.id">
        <ArtistPreview class="playlist" :name="artist.name" :image="artist.images[0]" :id="artist.id" :Albums="true" :playlist="playlistid"/>
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
  },
  data() {
    return {
      playlistid: "",
      allArtists: [],
      artistname: "",
    }
  },
    mounted() {
        this.playlistid = this.$route.params.id
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
