import os
import json

from .spotipy_auth import get_auth

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from spotipy import oauth2, Spotify



# AUTH VIEWS

def callback(request):
    # redirects here after Spotify login
    token = 'http://localhost:8000/callback/?{}'.format(request.GET.urlencode())

    sp_oauth = oauth2.SpotifyOAuth(os.getenv('SPOTIPY_CLIENT_ID'), os.getenv('SPOTIPY_CLIENT_SECRET'), os.getenv('SPOTIPY_REDIRECT_URI'), scope=os.getenv('SPOTIPY_SCOPE'))

    code = sp_oauth.parse_response_code(token)
    token_info = sp_oauth.get_access_token(code)

    if token_info:
        # store the Spotify token in the session
        request.session['spotipy_token'] = token_info
        print(request.session['spotipy_token'])

        sp = Spotify(auth= request.session['spotipy_token']['access_token'])
        request.session['user_id'] = sp.current_user()['id']

    return JsonResponse(request.session['spotipy_token'])


def login(request):
    sp_oauth = oauth2.SpotifyOAuth(os.getenv('SPOTIPY_CLIENT_ID'), os.getenv('SPOTIPY_CLIENT_SECRET'), os.getenv('SPOTIPY_REDIRECT_URI'), scope=os.getenv('SPOTIPY_SCOPE'))

    if 'spotipy_token' not in request.session:
        # if not logged in
        auth_url = sp_oauth.get_authorize_url(show_dialog=True)
        return HttpResponseRedirect(auth_url)

    return HttpResponse("Already logged in.")


def logout(request):
    # logs a user out of the app, not Spotify on browser
    response = HttpResponseRedirect('login')
    request.session.flush()

    return response


# OTHER VIEWS

def add_to_playlists(request):
    """Adds any number of tracks to all/ specified playlists, doesn't check for duplicates."""

    playlists = None  # HARDCODED
    track_ids = ["4ItljeeAXtHsnsnnQojaO2", "70gbuMqwNBE2Y5rkQJE9By"]  # HARDCODED

    user_id, _, sp = get_auth(request)

    if playlists is None:
        playlists = sp.user_playlists(user_id)['items']

    for playlist in playlists:
        if playlist['owner']['id'] == user_id:
            sp.user_playlist_add_tracks(user_id, playlist['id'], track_ids)

    return JsonResponse({'success': True})


def create_playlist(request):
    """Create a new playlist. Needs a title and optionally a description, collaborative boolean, public boolean, and image."""
    user_id, _, sp = get_auth(request)

    data = json.load(request)

    # create playlist with name and description
    playlist = sp.user_playlist_create(user_id, data["name"], description="")

    # set public and collaborative
    # sp.user_playlist_change_details(user_id, playlist['id'], public=False, collaborative=True)

    # add image
    # sp.playlist_upload_cover_image(playlist['id'], "image_b64")

    return JsonResponse(playlist)


def playlist(request, id):
    """Returns playlist details and details for its tracks."""
    user_id, _, sp = get_auth(request)

    return JsonResponse(sp.user_playlist(user_id, id, fields=None))


def playlists(request):
    """Returns all of a user's playlists."""
    _, _, sp = get_auth(request)
    results = sp.current_user_playlists(limit=50)

    # return JsonResponse(results['items'])
    return JsonResponse(results)


def merge_playlists(request):
    # Recover the data from the sent JSON, change as needed to work with UI
    # data = request.body
    # playlist_ids = data['playlist_ids']
    # new_playlist_name = data['new_playlist_name']

    # playlists Test1 and Test2 by DuckyDev
    playlist_ids = ["1q9tsT1RnrXRtLKBTri35F", "3LtqP8rfrFt9oyfgwVA2ff"]
    new_playlist_name = "Duck Test Playlist"

    # Set up the spotipy stuff
    user_id, _, sp = get_auth(request)

    # Get the songs from each of the playlists
    track_ids = []
    for playlist_id in playlist_ids:
        more_tracks = True
        offset = 0
        while more_tracks:
            # Get the next 100 tracks
            result = sp.playlist_tracks(playlist_id, offset=offset, limit=100)
            for item in result['items']:
                track_id = item['track']['id']
                track_ids.append(track_id)
            # Update more_tracks and the offset
            more_tracks = result['next'] != None
            offset += 100

    # Make a new playlist
    result = sp.user_playlist_create(user_id, name=new_playlist_name, public=False)
    new_playlist_id = result['id']

    # Add the list of songs to the new playlist
    offset = 0
    length = len(track_ids)
    while offset < length:
        sp.user_playlist_add_tracks(
            user_id, new_playlist_id, track_ids[offset:(offset+100)], position=offset)
        offset += 100

    # result = sp.user_playlist_add_tracks(user_id, new_playlist_id, track_ids[:100], position=offset)

    return JsonResponse({'success': True})
