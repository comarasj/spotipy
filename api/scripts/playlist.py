import sys
import spotipy
import spotipy.util as util
import os
import random
import subprocess
import scripts.settings as settings


def make_playlist(spotifyObject, user, tracks, playlist_name, long_playlist):
    playlist = spotifyObject.user_playlist_create(user, playlist_name, public=False)
    playlist_id = playlist['id']
    print(playlist_id)
    random_tracks = []
    if len(tracks) > 500:
        random_tracks = random.sample(tracks, 400)
    elif len(tracks) > 400:    
        random_tracks = random.sample(tracks, 300)
    elif len(tracks) > 300:
        random_tracks = random.sample(tracks, 200)
    elif len(tracks) > 200:
        random_tracks = random.sample(tracks, 100)
    elif len(tracks) > 100:
        random_tracks = random.sample(tracks, 100)
    else:
        spotifyObject.user_playlist_add_tracks(user, playlist_id, tracks, position=None)
        return playlist['uri']
    
    for i in range(int(len(random_tracks)/100)):
        spotifyObject.user_playlist_add_tracks(user, playlist_id, random_tracks[(i * 100):(((i+1)*100)-1)], position=None)
    return playlist['uri']


if __name__ == '__main__':
    scope = 'user-top-read user-read-private playlist-modify-private playlist-modify-public'
    token = util.prompt_for_user_token(settings.user,scope,client_id=settings.client_id,client_secret=settings.client_secret,redirect_uri=settings.redirect_uri)
    spotifyObject = spotipy.Spotify(auth=token)
