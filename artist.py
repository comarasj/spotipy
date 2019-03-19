import sys
import spotipy
import spotipy.util as util
import os
import subprocess
import settings as settings

scope = 'user-top-read user-read-private playlist-modify-private playlist-modify-public'

playlist_name = "helloworld"
playlist_description = "helloworld"

artists = ["Owl City", "Imagine Dragons", "Adam Young"]

token = util.prompt_for_user_token(settings.user,scope,client_id=settings.client_id,client_secret=settings.client_secret,redirect_uri=settings.redirect_uri)
spotifyObject = spotipy.Spotify(auth=token)

def get_artist_id(name):
    # Popularity greater than 30
    artist = spotifyObject.search(q='artist:' + name, type='artist')
    artist_id = []
    for i in artist['artists']['items']:
        if int(i['popularity']) > 30:
            artist_id.append(i['id'])
    return artist_id


if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    for i in artists:
        get_artist_id(i)
    # playlists = sp.user_playlist_create(settings.user, playlist_name, public=False)

else:
    print("Can't get token for", settings.user)