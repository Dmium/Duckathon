from django.urls import path

from . import views


urlpatterns = [
    # AUTH ENDPOINTS
    path('callback', views.callback, name='callback'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    # OTHER ENDPOINTS
    path('artist/<id>/albums', views.artist_albums, name='artist_albums'),
    path('artist/search', views.artist_search, name='artist_search'),

    path('nuke', views.nuke, name='nuke'),

    path('playlist/<id>', views.playlist, name='playlist'),
    path('playlists', views.playlists, name='playlists'),
    path('playlists/add', views.add_to_playlists, name='playlist_add'),
    path('playlists/add_albums', views.add_albums_to_playlist, name='playlists_add_albums'),
    path('playlists/clone', views.clone_playlist, name='playlist_clone'),
    path('playlists/create', views.create_playlist, name='playlist_create'),
    path('playlists/create/recent_tracks', views.create_from_recent_tracks, name='playlist_create_recent_tracks'),
    path('playlists/merge', views.merge_playlists, name='playlists_merge'),
    path('playlists/remove_by_keyword', views.remove_by_keyword, name='playlists_remove_keyword'),
    path('playlists/title_chain/<word>', views.title_chain, name='title_chain'),

    path('search/<type>/<query>', views.search, name='search'),
]
