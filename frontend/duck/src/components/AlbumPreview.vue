<template>
    <b-media tag="li">
        <template v-slot:aside>
            <div>
                <b-img v-if="image != null" :src="image.url" width="64" alt="placeholder"></b-img>
                <b-img v-if="image == null" src="https://image.flaticon.com/icons/svg/2284/2284983.svg" width="64" alt="placeholder"></b-img>
            </div>
            <div>
                <b-button v-if="addtoplaylist == true" size="lg" variant="primary" >Add to Playlist</b-button>
            </div>
        </template>

        <h5 class="mt-0">{{ this.name }}</h5>
    </b-media>
</template>

<script>

export default {
  name: 'album-preview',
  props: {
      id: String,
      name: String,
      image: Object,
      addtoplaylist: Boolean,
      playlist: String
  },
  methods: {
  },
}
</script>

