<template>
  <div class="playlists">
    <p>hi</p>
  </div>
</template>

<script>
// import PlaylistPreview from '../components/PlaylistPreview.vue';

export default {
  name: 'sampleposta',
  components: {
  },
  data() {
    return {
      playlist: {},
      tracks: []
    }
  },
  created() {
    this.$http.get('playlists')
      .then(response => {
        // JSON responses are automatically parsed.
        this.$http.post('sample', response.data)
            .then(response => {
                console.log(response.data)
            }).catch(e => {
                this.errors.push(e)
            })
      })
      .catch(e => {
        this.errors.push(e)
      })
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
</style>
