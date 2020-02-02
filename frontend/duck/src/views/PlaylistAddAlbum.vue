<template>
  <div>

    <h1>Search for an artist</h1>
    <b-form class="new-playlist-form" @submit="onSubmit">
      <b-form-group>
        <b-form-input
          id="new-playlist-input"
          v-model="artistname"
          required
          placeholder="Enter an artist name"
          size="lg"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary" size="lg">Submit</b-button>
    </b-form>

    <br/>
    <br/>
    <div v-for="artist in allArtists" :key="artist.id">
        <ArtistPreview class="playlist" :name="artist.name" :image="artist.images[0]" :id="artist.id" :Albums="true" :playlist="playlistid"/>
    </div>

  </div>
</template>

<script>

import ArtistPreview from '../components/ArtistPreview.vue';

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
    onSubmit() {
        this.$http.get('search/artist/' + this.artistname)
            .then(response => {
                this.allArtists = response.data.artists.items
            })
            .catch(e => {
                this.errors.push(e)
            })
    }
  },
}
</script>
