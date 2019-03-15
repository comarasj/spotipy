import sys
import spotipy
import spotipy.util as util
# import setup
import os
import subprocess


scope = 'user-top-read user-read-private playlist-modify-private playlist-modify-public'

# if len(sys.argv) > 3:
username = "Stephen Comaraata"
username = "1255822034"
playlist_name = "Test"
playlist_description = "helloworld"
#     playlist_id = "2018"
#     track_ids = ""
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()

token = util.prompt_for_user_token(username,scope,client_id='a6c7402240df4a8486ec522cb82a2ba7',client_secret='5d142ecd5cfc4308852aaa5e477115e0',redirect_uri='http://localhost/')
spotifyObject = spotipy.Spotify(auth=token)


if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    # artists = ['Owl City']
    # artists = getArtistIds(artists)
    # print(artists)
    
    
    playlists = sp.user_playlist_create(username, playlist_name, public=False)
    



else:
    print("Can't get token for", username)