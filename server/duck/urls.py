from django.urls import path

from . import views


urlpatterns = [
    path('test', views.test_page, name='test_page'),

    path('callback', views.callback, name='callback'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('playlists', views.playlists, name='playlists'),
    path('playlists/add', views.add_to_playlists, name='playlists_add'),
    path('playlists/<id>', views.playlist, name='playlist'),
    path('playlists/merge', views.merge_playlists, name='playlists_merge'),
]
