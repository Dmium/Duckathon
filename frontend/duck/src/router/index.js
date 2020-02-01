import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import AllPlaylists from '../views/AllPlaylists.vue'
import Playlist from '../views/Playlist.vue'
import NewPlaylist from '../views/NewPlaylist.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/playlists',
        name: 'playlists',
        component: AllPlaylists
    },
    {
        path: '/playlists/get/:id',
        name: 'playlist',
        component: Playlist
    },
    {
        path: '/playlists/new',
        name: 'newplaylist',
        component: NewPlaylist
    }
]

const router = new VueRouter({
    routes
})

export default router