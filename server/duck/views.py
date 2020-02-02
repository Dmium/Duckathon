import os
import json

from .spotipy_auth import get_auth

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
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

        sp = Spotify(auth= request.session['spotipy_token']['access_token'])
        request.session['user_id'] = sp.current_user()['id']

    return redirect("http://localhost:8080/#/playlists")


def login(request):
    sp_oauth = oauth2.SpotifyOAuth(os.getenv('SPOTIPY_CLIENT_ID'), os.getenv('SPOTIPY_CLIENT_SECRET'), os.getenv('SPOTIPY_REDIRECT_URI'), scope=os.getenv('SPOTIPY_SCOPE'))

    if 'spotipy_token' not in request.session:
        # if not logged in
        auth_url = sp_oauth.get_authorize_url(show_dialog=True)
        return HttpResponseRedirect(auth_url)

    return redirect("http://localhost:8080/#/playlists")


def logout(request):
    # logs a user out of the app, not Spotify on browser
    response = HttpResponseRedirect('login')
    request.session.flush()

    return redirect("http://localhost:8080/#/")


# OTHER VIEWS

def add_albums_to_playlist(request):
    """Add all tracks from the provided albums to a specified playlist."""

    data = json.load(request)
    playlist_id = data['playlist_id']
    album_ids = data['album_ids']

    user_id, _, sp = get_auth(request)

    # For each album ID, get the track IDs and store them
    track_ids = []
    for album_id in album_ids:
        more_tracks = True
        offset = 0
        while more_tracks:
            # Get the next 50 tracks
            result = sp.album_tracks(album_id, offset=offset, limit=50)
            for item in result['items']:
                track_id = item['id']
                track_ids.append(track_id)
            # Update more_tracks and the offset
            more_tracks = result['next'] != None
            offset += 50

    # Add the tracks to the specified playlist
    offset = 0
    length = len(track_ids)
    while offset < length:
        sp.user_playlist_add_tracks(user_id, playlist_id, track_ids[offset:(offset+100)], position=offset)
        offset += 100

    return JsonResponse({'success': True})


def add_to_playlists(request):
    """Adds any number of tracks to all playlists, doesn't check for duplicates."""
    data = json.load(request)
    track_id = data['id']

    user_id, _, sp = get_auth(request)

    playlists = sp.user_playlists(user_id)['items']

    for playlist in playlists:
        if playlist['owner']['id'] == user_id:
             sp.user_playlist_add_tracks(user_id, playlist['id'], [track_id])

    return JsonResponse({'success': True})


def artist_albums(request, id):
    """Return all of an artist's albums, sorted by album type."""

    _, _, sp = get_auth(request)
    
    artist_id = id

    result_a = sp.artist_albums(artist_id, album_type="album", country="GB", limit=50)
    result_b = sp.artist_albums(artist_id, album_type="single", country="GB", limit=50)
    result_c = sp.artist_albums(artist_id, album_type="appears_on", country="GB", limit=50)
    result_d = sp.artist_albums(artist_id, album_type="compilation", country="GB", limit=50)

    result = {
        "albums": result_a['items'],
        "singles": result_b['items'],
        "appears_ons": result_c['items'],
        "compilations": result_d['items'],
    }

    return JsonResponse(result)


def artist_search(request):
    """Return the top 5 (or less) search results for an artist."""

    # Fake input
    artist_name = "Carly Rae"

    _, _, sp = get_auth(request)

    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artists = items[:5]
        return JsonResponse({'success': True, 'results': artists})
    else:
        return JsonResponse({'success': False})


def clone_playlist(request):
    user_id, _, sp = get_auth(request)

    # data = json.load(request)
    data = {'id':'1q9tsT1RnrXRtLKBTri35F'}

    # get data of original playlist
    original = sp.user_playlist(user_id, data['id'])

    # creation with name and description
    clone = sp.user_playlist_create(user_id, original['name']+" - Clone", description=original['description'])

    # setting public and collaborative
    sp.user_playlist_change_details(user_id, clone['id'], public=original['public'], collaborative=original['collaborative'])

    # add tracks
    track_ids = []
    more_tracks = True
    offset = 0
    while more_tracks:
        # Get the next 100 tracks
        result = sp.playlist_tracks(original['id'], offset=offset, limit=100)
        for item in result['items']:
            track_id = item['track']['id']
            track_ids.append(track_id)
        # Update more_tracks and the offset
        more_tracks = result['next'] != None
        offset += 100

    # Add the list of songs to the new playlist
    offset = 0
    length = len(track_ids)
    while offset < length:
        sp.user_playlist_add_tracks(
            user_id, clone['id'], track_ids[offset:(offset+100)], position=offset)
        offset += 100

    return JsonResponse(sp.playlist(clone['id']))


def create_playlist(request):
    """Create a new playlist. Needs a title and optionally a description, collaborative boolean, public boolean, and image."""
    user_id, _, sp = get_auth(request)

    data = json.load(request)

    # create playlist with name and description
    playlist = sp.user_playlist_create(user_id, data["name"], description="")

    # set public and collaborative
    # sp.user_playlist_change_details(user_id, playlist['id'], public=False, collaborative=True)

    return JsonResponse(playlist)


def create_from_recent_tracks(request):
    user_id, _, sp = get_auth(request)

    items = sp.current_user_recently_played(limit=50)['items']

    if len(items) != 0:
        playlist_id = sp.user_playlist_create(user_id, "Recent Tracks", description="Contains the tracks you've listened to recently.")['id']

        track_ids = set([item['track']['id'] for item in items])

        sp.user_playlist_add_tracks(user_id, playlist_id, track_ids)

        return JsonResponse({'success': True})

    return JsonResponse({'message': 'No recent tracks.'})


def merge_playlists(request):
    """Create a new playlist by merging the contents of multiple playlists."""

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


def nuke(request):
    """Remove the provided song from all playlists a user owns."""

    data = json.load(request)
    track_id = data['id']

    user_id, _, sp = get_auth(request)

    playlists = sp.user_playlists(user_id)['items']

    for playlist in playlists:
        if playlist['owner']['id'] == user_id:
            sp.user_playlist_remove_all_occurrences_of_tracks(user_id, playlist['id'], [track_id])

    return JsonResponse({'success': True})


def playlist(request, id):
    """Returns playlist details and details for its tracks."""
    user_id, _, sp = get_auth(request)

    results = sp.user_playlist(user_id, id)
    return JsonResponse(results)


def playlists(request):
    """Returns all of a user's playlists."""
    _, _, sp = get_auth(request)
    results = sp.current_user_playlists(limit=50)

    # return JsonResponse(results['items'])
    return JsonResponse(results)


def remove_by_keyword(request):
    """Remove all tracks from a playlist whose name contains the provided target word."""

    def word_in_track_name(word, track_name):
        return word.lower() in track_name.lower()

    user_id, _, sp = get_auth(request)

    # Get input from frontend
    # target_word = ?
    # playlist_id = ?

    # Fake input - REMOVE WHEN FRONTEND IS LINKED
    target_word = "Version"
    playlist_id = "6JW6em51gITQVoMZpcjVHL"

    # Get the playlist track info and store IDs of songs matching criteria
    track_ids = []
    more_tracks = True
    offset = 0
    while more_tracks:
        # Get the next 100 tracks
        result = sp.user_playlist_tracks(
            user_id, playlist_id, offset=offset, limit=100)
        for item in result['items']:
            track_name = item['track']['name']
            if word_in_track_name(target_word, track_name):
               track_id = item['track']['id']
               track_ids.append(track_id)
        # Update more_tracks and the offset
        more_tracks = result['next'] != None
        offset += 100

    # Remove all occurrences of tracks with cursed IDs
    sp.user_playlist_remove_all_occurrences_of_tracks(
        user_id, playlist_id, track_ids)

    return JsonResponse({'success': True})


def search(request, type, query):
    """Searches for a record of type (album, artist, track, playlist) similar to the query string."""

    _, _, sp = get_auth(request)

    results = sp.search(query, limit=10, type=type, market="GB")
    return JsonResponse(results)
