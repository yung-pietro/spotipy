import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.util import prompt_for_user_token

client_id = '866e67d3c5924baca1114ed5bc4eef50'
client_secret = 'c6e2baa4ecac47cc9ecd6bf7dced31f4'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print(sp.me())
exit()

playlists = sp.current_user_playlists()
print(playlists)
exit()

#How do I obscure these so that they can't be seen by public eyes

credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials_manager)
# Question is, why do we need to import SpotifyClientCredentials, but not spotipy.Spotify

# I want to be able to output all playlist IDs and names from this account
# print(sp.current_user())
# exit()
playlists = sp.user_playlists('spotify')
print(playlists)
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
