<template>
  <div id="app">
    <NavBar/>
    <div id="content">
      <router-view/>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';

export default {
  name: 'app',
  components: {
    NavBar
  }
}
</script>

<style lang="scss">

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #FFFFFF;
  background-color: #191414;
  height: 100%;
  min-height: 100vh;
}

#content {
  height: 100%;
  min-height: 95vh
}
</style>
