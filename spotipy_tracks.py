import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from pprint import pprint
import os


os.environ["SPOTIPY_CLIENT_ID"] = "855993e513334a8bb6e0f27794d65e76"
os.environ["SPOTIPY_CLIENT_SECRET"] = "032d2a9e371b417f9df837c25fdb69a3"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://google.com/"
#https://docs.python.org/3/library/os.html#os.environ
# Why do we set these variables this way, vs simply declaring them?



username = "1252709106"
# Get the username from terminal
scope = "user-read-private"

# User ID: 1252709106
# SPOTIPY_CLIENT_ID='866e67d3c5924baca1114ed5bc4eef50'
# SPOTIPY_CLIENT_SECRET='c6e2baa4ecac47cc9ecd6bf7dced31f4'
# SPOTIPY_REDIRECT_URI='http://google.com'


# erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
    print(token)
    #try clause runs.
    # BQA0S0vgtn2ieFYYFmImyy7r8KN5EsFkwzoZae6aDVTfqSCVkDwgsv4Y7cCJyiozVO7VSMk9O4y1Kopy5OiWdI6WhFpZt3YqphnNgaMH2O90fdn4_xP8avv71dsKivkB7PRdKl81rjbXWqILIWEJpe8sYaTgpcCOKQ
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope)

# Create Spotify Object
sp = spotipy.Spotify(auth=token)
pprint(sp.current_user_recently_played(limit=50))
#ppprint is a specially formatted print clause
#I keep getting: AttributeError: 'Spotify' object has no attribute 'current_user_recently_played'

# for dealing with JSON
# print(json.dumps(VARIABLE, sort_keys = True, indent = 4))
