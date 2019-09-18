import os
import sys
import json
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser
from json.decoder import JSONDecodeError
from pprint import pprint
import os


client_id = "866e67d3c5924baca1114ed5bc4eef50"
client_secret = "c6e2baa4ecac47cc9ecd6bf7dced31f4"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = "1252709106"
playlist_id = '37i9dQZF1E8Gd0iQSccTIC'
offset = 0


results = sp.user_playlist_tracks(username, playlist_id, fields=None, limit=100, offset=offset, market=None)
# pprint(results)
# exit()
print(json.dumps(results, indent=4))
