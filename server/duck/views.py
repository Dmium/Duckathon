from django.shortcuts import render, HttpResponseRedirect
import spotipy
# import spotipy.util as util
from django.http import HttpResponse
from spotipy import oauth2


# Create your views here.
def test_page(request):
    return render(request, 'duck/example.html')

def callback(request):
    return render(request, 'duck/example.html')

def next_offset(n):
    try:
        return int(n['next'].split('?')[1].split('&')[0].split('=')[1])
    except ValueError:
        return None
    except AttributeError:
        return None
    except TypeError:
        return None

def login(request):
    scope = 'user-library-read'

    # if len(sys.argv) > 1:
    #     username = sys.argv[1]
    # else:
    #     print("Usage: %s username" % (sys.argv[0],))
    #     sys.exit()
    
    # username = 'jumeist'

    # token = util.prompt_for_user_token(username, scope, client_id='',
    # client_secret='',
    # redirect_uri='')

    # if token:
    #     sp = spotipy.Spotify(auth=token)
    #     results = sp.current_user_saved_tracks()
    #     for item in results['items']:
    #         track = item['track']
    #         return HttpResponse(track['name'] + ' - ' + track['artists'][0]['name'])
    # else:
    #     return HttpResponse("Can't get token for", username)

    # token = util.prompt_for_user_token(username, scope)
    # print(token)

    scope = 'user-library-read'

    sp_oauth = oauth2.SpotifyOAuth('client_id', 'secret_client_id', 'redirect_uri', scope=scope)

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        return HttpResponseRedirect(auth_url)

    sp = spotipy.Spotify(auth=token_info['access_token'])
    total = []
    results = sp.current_user_saved_tracks(limit=50)
    next = next_offset(results)

    total.append(results)
    while next and next < int(results['total']):
        next_50 = sp.current_user_saved_tracks(limit=50, offset=next)
        next = next_offset(next_50)
        total.append(next_50)
        print(next)
    tracks = []
    for r in total:
        for track in r['items']:
            tracks.append(track)

    # return render(request, 'pages/sign-in.html', {'results': tracks})

    return HttpResponse(tracks)