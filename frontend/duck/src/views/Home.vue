<template>
  <div class="home">
    <div class="landing-page">
      <br />
      <div class="landing-text">
        <h1 id="header-text">Take control of your music</h1>
        <p id="secondary-text">Create playlists intelligently with Duckify</p>
        <b-button size="lg" variant="primary" href="http://localhost:8000/login">Log in to Spotify</b-button>
        <b-table striped hover
        :items="items"
        />
      </div>
    </div>
  </div>
</template>

<script>

// import axios from 'axios';
export default {
  name: 'home',
  data () {
    return {
      errors: [],
      items: []
    }
  },
  created() {
    this.$http.get('login', {withCredentials: true})
      .catch(e => {
        this.errors.push(e)
      })
    this.$http.get('playlists', {withCredentials: true})
      .then(response => {
        // JSON responses are automatically parsed.
          console.log('notbad')
        this.items = response.data.items
      })
      .catch(e => {
          console.log('bad')
        this.errors.push(e)
      })
    }
}
</script>

<style lang="scss">

.landing-page {
  background-image: url("../assets/landing-img.svg");
	background-size: contain;
  background-repeat: no-repeat;
  background-position: right center;
  height: 85vh;
  text-align: left;
}

.landing-text {
  margin-left: 5%;
  margin-top: 5%;
  width: 40%;
}

#header-text {
  font-size: 450%;
}

#secondary-text {
  font-size: 20pt;
  width: 80%;
}
</style>
