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
import ReverseNuke from '../views/Tools/ReverseNuke.vue'
import PlaylistRemoveKeyword from '../views/PlaylistRemoveKeyword.vue'
import Artist from '../views/Artist.vue'
import RecentsPlaylist from '../views/Tools/RecentsPlaylist.vue'
import PlaylistChain from '../views/PlaylistChain.vue'

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
        path: '/playlist/:id/add/album/:name',
        name: 'playlistaddalbum',
        component: PlaylistAddAlbum
    },
    {
        path: '/playlist/:id/remove/keyword',
        name: 'removebykeyword',
        component: PlaylistRemoveKeyword
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
    },
    {
        path: '/tools/reversenuke',
        name: 'reversenuke',
        component: ReverseNuke
    },
    {
        path: '/addalbum/:playlistid/:artistid',
        name: 'artist',
        component: Artist
    },
    {
        path: 'tools/recentsplaylist',
        name: 'recentsplaylist',
        component: RecentsPlaylist
    },
    {
        path: '/playlistchain',
        name: 'playlistchain',
        component: PlaylistChain
    }
]

const router = new VueRouter({
    routes
})

export default router