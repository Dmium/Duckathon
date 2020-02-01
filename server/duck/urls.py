from django.urls import path

from . import views


urlpatterns = [
    path('test', views.test_page, name='test_page'),

    path('add_to_playlists', views.add_to_playlists, name='add_to_playlists'),
    path('callback', views.callback, name='callback'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('playlists', views.playlists, name='playlists'),
    path('playlists_merge', views.playlists_merge, name='playlists_merge'),
]
