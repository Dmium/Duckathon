import os
import spotipy

from spotipy import oauth2, util


def refresh_token(request):
    sp_oauth = oauth2.SpotifyOAuth(os.getenv('SPOTIPY_CLIENT_ID'), os.getenv('SPOTIPY_CLIENT_SECRET'), os.getenv('SPOTIPY_REDIRECT_URI'), scope=os.getenv('SPOTIPY_SCOPE'))

    # store the refreshed token
    request.session['spotipy_token'] = sp_oauth.refresh_access_token(request.session['spotipy_token']['refresh_token'])

    return request.session['spotipy_token']['access_token']

def get_auth(request):
    user_id = request.session['user_id']
    token = refresh_token(request)
    sp = spotipy.Spotify(auth=token)

    return user_id, token, sp