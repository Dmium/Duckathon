import os
import spotipy

from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from spotipy import oauth2


# Create your views here.
def test_page(request):
    return render(request, 'duck/example.html')


def callback(request):
    # redirects here after Spotify login
    token = 'http://localhost:8000/callback/?{}'.format(request.GET.urlencode())

    sp_oauth = oauth2.SpotifyOAuth(os.getenv('SPOTIPY_CLIENT_ID'), os.getenv('SPOTIPY_CLIENT_SECRET'), os.getenv('SPOTIPY_REDIRECT_URI'), scope=os.getenv('SPOTIPY_SCOPE'))

    code = sp_oauth.parse_response_code(token)
    token_info = sp_oauth.get_access_token(code)

    if token_info:
        # store the Spotify token in the session
        request.session['spotify_token'] = token_info['access_token']

    return HttpResponse(request.session['spotify_token'])


def login(request):
    sp_oauth = oauth2.SpotifyOAuth(os.getenv('SPOTIPY_CLIENT_ID'), os.getenv('SPOTIPY_CLIENT_SECRET'), os.getenv('SPOTIPY_REDIRECT_URI'), scope=os.getenv('SPOTIPY_SCOPE'))

    if 'spotify_token' not in request.session:
        # if not logged in
        auth_url = sp_oauth.get_authorize_url()
        return HttpResponseRedirect(auth_url)

    return HttpResponse("Already logged in.")
