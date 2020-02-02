import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import AllPlaylists from '../views/AllPlaylists.vue'
import Playlist from '../views/Playlist.vue'
import NewPlaylist from '../views/NewPlaylist.vue'
import SamplePosta from '../views/SamplePosta.vue'
import PlaylistAddAlbum from '../views/PlaylistAddAlbum.vue'
import Tools from '../views/Tools.vue'
import Nuke from '../views/Tools/Nuke.vue'

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
    },
    {
        path: '/sampleposta',
        name: 'sampleposta',
        component: SamplePosta
    },
    {
        path: '/playlist/:id/add/album',
        name: 'playlistaddalbum',
        component: PlaylistAddAlbum
    },
    {
        path: '/tools',
        name: 'tools',
        component: Tools
    },
    {
        path: '/tools/nuke',
        name: 'nuke',
        component: Nuke
    }
]

const router = new VueRouter({
    routes
})

export default router