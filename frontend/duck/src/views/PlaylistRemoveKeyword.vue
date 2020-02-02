<template>
  <div>
    <h1>Remove all songs with a word in their title</h1>
    <b-form class="keyword-form" @submit="onSubmit">
      <b-form-group>
        <b-form-input
          id="keyword-input"
          v-model="keyword"
          required
          placeholder="Enter a keyword; live, alternate, version, etc"
          size="lg"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary" size="lg">Submit</b-button>
    </b-form>

    <h2>{{ num_removed }}</h2>
  </div>
</template>

<script>
export default {
  name: 'removebykeyword',
  // props: {
  //     id: String
  // },
  data() {
    return {
      keyword: "",
      playlist_id: "",
      num_removed: null,
    }
  },
  mounted() {
    this.playlist_id = this.$route.params.id
  },
  methods: {
    onSubmit() {
      this.$http.post('playlists/remove_by_keyword', {
        keyword: this.keyword,
        playlist_id: this.playlist_id})
      setTimeout( () => this.$router.push({ name: "playlist"}), 500)
    }
  }
}
</script>

<style>

</style>
