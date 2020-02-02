<template>
  <div>
    <h1>Albums</h1>
    
  </div>
</template>

<script>

export default {
  name: 'artist',
  components: {
  },
  data() {
    return {
      allAlbums: [],
      artistid: "",
    }
  },
  mounted() {
    this.artistid = this.$route.params.artistid
    this.$http.get('artist/' + this.artistid + '/albums')
    .then(response => {
        this.allAlbums = response.data.items
    })
    .catch(e => {
        this.errors.push(e)
    })
  },
  methods: {
  }
}
</script>

<style>
</style>
