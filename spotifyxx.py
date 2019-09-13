import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
username = sys.argv[1]

# User ID: 1252709106
# SPOTIPY_CLIENT_ID='866e67d3c5924baca1114ed5bc4eef50'
# SPOTIPY_CLIENT_SECRET='c6e2baa4ecac47cc9ecd6bf7dced31f4'
# SPOTIPY_REDIRECT_URI='http://google.com'


# erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)



# for dealing with JSON
# print(json.dumps(VARIABLE, sort_keys = True, indent = 4))
