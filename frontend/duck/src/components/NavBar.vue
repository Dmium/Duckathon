<template>
  <div>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand><router-link class="white-text" :to="{name: 'home'}">Duckify for</router-link> <a href="https://www.spotify.com/"><img id="spotify-logo" src="../assets/spotify-logo.png"/></a></b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/">Get Started</b-nav-item>
        <b-nav-item to="/playlists">Playlists</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>

export default {
  name: 'navbar'
}
</script>

<style lang="scss">

#spotify-logo {
  width: 30px;
}

.white-text, .white-text:hover {
  color: var(--spotify-white);
  text-decoration: none;
}
</style>
