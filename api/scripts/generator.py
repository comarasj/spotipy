import sys
import spotipy
import spotipy.util as util
import os
import subprocess
import scripts.settings as settings

import scripts.artist as artist
import scripts.playlist as playlist



scope = 'user-top-read user-read-private playlist-modify-private playlist-modify-public'




token = util.prompt_for_user_token(settings.user,scope,client_id=settings.client_id,client_secret=settings.client_secret,redirect_uri=settings.redirect_uri)
spotifyObject = spotipy.Spotify(auth=token)


def main(playlist_name, artists):
    artist_ids = []
    rel_artists = []
    all_artists = []
    tracks = []
    dup_tracks = []
    all_tracks = []

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        for i in artists:
            artist_ids.append(artist.get_id(spotifyObject, i))
        for id in artist_ids:
            all_artists.append(id)
            rel_artists.append(artist.get_rel_id(spotifyObject, id))
        for i in rel_artists:
            for id in i:
                all_artists.append(id)
        
        for artist_id in all_artists:
            tracks.append(artist.get_top_tracks(spotifyObject, artist_id))

        for i in tracks:
            for uri in i:
                if uri not in dup_tracks:
                    dup_tracks.append(uri)
                    all_tracks.append(uri)
        
        print(all_tracks)
        return playlist.make_playlist(spotifyObject, settings.user, all_tracks, playlist_name, True)
        # playlists = sp.user_playlist_create(settings.user, playlist_name, public=False)


    else:
        print("Can't get token for", settings.user)


if __name__ == '__main__':
    playlist_name = "Awesome Playlist "
    artists = ["Thomas Rhett", "Owl City", "Demi Lovato"]
    main(playlist_name, artists)