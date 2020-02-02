from django.urls import path

from . import views


urlpatterns = [
    # AUTH ENDPOINTS
    path('callback', views.callback, name='callback'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    # OTHER ENDPOINTS
    path('playlist/<id>', views.playlist, name='playlist'),
    path('playlists', views.playlists, name='playlists'),
    path('playlists/add', views.add_to_playlists, name='playlists_add'),
    path('playlists/create', views.create_playlist, name='playlist_create'),
    path('playlists/merge', views.merge_playlists, name='playlists_merge'),
    path('playlists/remove_by_keyword', views.remove_by_keyword, name='playlists_remove_keyword'),
    path('playlist/add_albums', views.add_albums_to_playlist, name='playlists_add_albums'),

    path('artist/albums', views.artist_albums, name='artist_albums'),
    path('artist/search', views.artist_search, name='artist_search'),

    path('search/<type>/<query>', views.search, name='search'),
]
