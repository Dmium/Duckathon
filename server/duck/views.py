from . import keys

import os

from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from spotipy import oauth2


# Create your views here.
def test_page(request):
    return render(request, 'duck/example.html')

def callback(request):
    return HttpResponse("Successfully logged in.")

def login(request):
    scope = 'user-library-read'

    sp_oauth = oauth2.SpotifyOAuth(keys.SPOTIFY_CLIENT_ID, keys.SPOTIFY_CLIENT_SECRET, keys.SPOTIFY_REDIRECT_URI, scope=scope)

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        return HttpResponseRedirect(auth_url)

    return HttpResponse("Already logged in.")