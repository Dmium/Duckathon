<template>
  <div>
    <p>{{this.id}}</p>
    
  </div>
</template>

<script>

export default {
  name: 'playlistaddalbum',
  components: {
  },
  props: {
      id: String
  },
  data() {
    return {
      playlist: {},
      tracks: []
    }
  },
  created() {
    this.id = this.$route.params.id
  }
}
</script>
