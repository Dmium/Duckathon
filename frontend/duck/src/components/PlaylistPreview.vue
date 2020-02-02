<template>
    <div class="playlist">
        <img class="album-icon-lg" v-if="image != null" :src="image"/>
        <img v-else src="https://image.flaticon.com/icons/svg/2284/2284983.svg"/>
        <h5>{{ title }}</h5>
        <router-link :to="{ name: 'playlist', params: {id: this.id } }">Edit</router-link>
    </div>
</template>

<script>

export default {
  name: 'playlist-preview',
  props: {
      id: String,
      title: String,
      description: String,
      image: String
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
    margin-top: 2rem;
    margin-bottom: 2rem;
}
</script>
