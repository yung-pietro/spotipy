# import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials


client_id = '866e67d3c5924baca1114ed5bc4eef50'
client_secret = 'bea4c0cb0923458b8e2c57451d126652'
#How do I obscure these so that they can't be seen by public eyes

credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
#credentials_manager is a new *object* from the SpotifyClientCredentials *class*.  
# To understand more about the class, we can search in the Spotipy docs: https://spotipy.readthedocs.io/en/latest/?highlight=spotifyclientcredentials#spotipy.oauth2.SpotifyClientCredentials
# Or search in the codebase.  All module files reside in the site-packages folder

# sp = spotipy.Spotify(client_credentials_manager=credentials_manager)
sp = Spotify(client_credentials_manager=credentials_manager)
#This instantiates a new Spotify object (def found  \lib\python3.7\site-packages\spotipy\client.py)

# I want to be able to output all playlist IDs and names from this account
# print(sp.current_user())
# exit()

playlist_results = sp.current_user_playlists()

#How is the spotipy module related to the the Spotify API call?
# https://spotipy.readthedocs.io/en/latest/#module-spotipy.client
#  I think I need a value for `username` in the () above.  How do I call it, and how do I know what 

#print(playlist_results)
# print(playlist_results['name'] ['id'] [0])

"""
playlist_loop = sp.user_playlists('spotify')
while playlist_loop:
    for i, playlist_loop in enumerate(playlist_loop['items']):
        print ("%4d %s %s" % (i + 1 playlist_loop['offset'], playlist_loop['id'], playlist_loop['name']))
    if playlist_loop['next']:
        playlist_loop = sp.next(playlist_loop)
    else:
        playlist_loop = None
"""
# I found this inside the spotipy documentation - but I guess I'm unlcear as to why I would need to run a loop, when supposedly line 14 would output
# everything on its own.

# I then want to output all tracks in a playlist based on playlist ID
# https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlists-tracks/
