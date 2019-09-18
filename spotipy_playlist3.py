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


os.environ["SPOTIPY_CLIENT_ID"] = "866e67d3c5924baca1114ed5bc4eef50"
os.environ["SPOTIPY_CLIENT_SECRET"] = "c6e2baa4ecac47cc9ecd6bf7dced31f4"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://google.com/"
#https://docs.python.org/3/library/os.html#os.environ
# Why do we set these variables this way, vs simply declaring them?


username = "1252709106"
# Get the username from terminal
# scope = "user-read-private"
scope = "playlist-read-private"

# erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
    print(token)
    #try clause runs.
    # BQA0S0vgtn2ieFYYFmImyy7r8KN5EsFkwzoZae6aDVTfqSCVkDwgsv4Y7cCJyiozVO7VSMk9O4y1Kopy5OiWdI6WhFpZt3YqphnNgaMH2O90fdn4_xP8avv71dsKivkB7PRdKl81rjbXWqILIWEJpe8sYaTgpcCOKQ
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

# Create Spotify Object
sp = spotipy.Spotify(auth=token)
# pprint(sp.current_user_playlists())
#ppprint is a specially formatted print clause

# for dealing with JSON
# print(json.dumps(VARIABLE, sort_keys = True, indent = 4))

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:1252709106:spotifycharts:playlist:37i9dQZEVXbJiZcmkrIHGU'
# print(uri.split(":"))
#username = uri.split(':')[1]
#playlist_id = uri.split(':')[4]


playlist_id = '37i9dQZEVXbJiZcmkrIHGU'

print(username)
results = sp.user_playlist(username)
print(results)
print(json.dumps(results, indent=4)[0])
