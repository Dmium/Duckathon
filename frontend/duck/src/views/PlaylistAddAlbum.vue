<template>
  <div>
    <p>{{id}}</p>
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
  }
}
</script>
