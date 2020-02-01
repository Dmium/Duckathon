<template>
  <div class="home">
    <div class="landing-page">
      <br />
      <div class="landing-text">
        <h1 id="header-text">Take control of your music</h1>
        <p id="secondary-text">Create playlists intelligently with Duckify</p>
        <b-button size="lg" variant="primary" to="/login">Log in to Spotify</b-button>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'home'
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
