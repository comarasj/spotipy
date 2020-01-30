import sys
import spotipy
import spotipy.util as util
import os
import subprocess
import scripts.settings as settings



def get_id(spotifyObject, name):
    '''
    Return most popular artist id
    '''
    artist = spotifyObject.search(q='artist:' + name, type='artist')
    artist_pop = 0
    if artist['artists']['items']:
        for i in artist['artists']['items']:
            if i['popularity'] > artist_pop:
                artist_id = i['id']
                artist_pop = i['popularity']
        return artist_id


def get_rel_id(spotifyObject, id):
    query = spotifyObject.artist_related_artists(id)
    rel_artist_id = []
    for i in query['artists']:
        if int(i['popularity']) > 40:
            rel_artist_id.append(i['id'])
    return rel_artist_id


def get_top_tracks(spotifyObject, id):
    top_tracks = []
    query = spotifyObject.artist_top_tracks(id, country='US')
    for i in query['tracks']:
        top_tracks.append(i['id'])
    return top_tracks


def get_recommendations(spotifyObject, ids):
    return spotifyObject.recommedations(seed_artists=ids, seed_genres=None, seed_tracks=None, limit=100, country=None)


if __name__ == '__main__':
    scope = 'user-top-read user-read-private playlist-modify-private playlist-modify-public'
    token = util.prompt_for_user_token(settings.user,scope,client_id=settings.client_id,client_secret=settings.client_secret,redirect_uri=settings.redirect_uri)
    spotifyObject = spotipy.Spotify(auth=token)
    
    
