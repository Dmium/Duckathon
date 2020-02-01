import os
import spotipy

from django.http import HttpResponse, JsonResponse
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
        auth_url = sp_oauth.get_authorize_url(show_dialog=True)
        return HttpResponseRedirect(auth_url)

    return HttpResponse("Already logged in.")


def logout(request):
    # logs a user out of the app, not Spotify on browser
    response = HttpResponseRedirect('test')
    request.session.flush()

    return response


def playlists(request):
    token = request.session['spotify_token']
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_playlists(limit=50)

    # return JsonResponse(results['items'])
    return JsonResponse(results)


def playlists_merge(request):
    # Recover the data from the sent JSON, change as needed to work with UI
    # data = request.body
    # playlist_ids = data['playlist_ids']
    # new_playlist_name = data['new_playlist_name']
    playlist_ids = ["37i9dQZF1DX0Yxoavh5qJV", "66nCEou08JgGmApr3UHzIZ"]
    new_playlist_name = "Duck Test Playlist"

    # Set up the spotipy stuff
    token = request.session['spotify_token']
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    
    # Get the songs from each of the playlists
    track_ids = []
    for playlist_id in playlist_ids:
        results = sp.playlist_tracks(playlist_id, limit=100)
        for item in results['items']:
            track_id = item['track']['id']
            track_ids.append(track_id)

    # Get the user id - could do earlier and store in session
    result = sp.current_user()
    user_id = result['id']

    # Make a new playlist
    result = sp.user_playlist_create(user_id, name=new_playlist_name, public=False)
    new_playlist_id = result['id']

    # Add the list of songs to the new playlist
    result = sp.user_playlist_add_tracks(user_id, new_playlist_id, track_ids[:100])

    return JsonResponse(result)
