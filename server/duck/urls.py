from django.urls import path

from . import views

urlpatterns = [
    path('test', views.test_page, name='test_page'),
    path('callback', views.callback, name='callback'),
    path('login', views.login, name='login'),
    path('playlists', views.playlists, name='playlists'),
    path('playlists_merge', views.playlists_merge, name='playlists_merge'),
]
