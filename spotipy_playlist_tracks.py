import json
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import pandas as pd

with open('config.json') as config_file:
    data = json.load(config_file)

client_id = data['id']
client_secret = data['secret']

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = data['username']
playlist_id = data['playlist_id']
offset = data['offset']


results = sp.user_playlist_tracks(username, playlist_id, fields=None, limit=100, offset=offset, market=None)
# Currently outputs a dictionary with (embedded lists and dicts) containing track info.  Things like identifying URI, album art, etc.
# I will use this to loop through each track listing and, using the identifying URI, grab track info.

# print(results['items'][0]['track']['id'])
#demo accessing a single track id

# print the type of the object
# print(type(results['items']))



track_attributes = {
                    'track_name': [],
                    'track_id': [],
                    'album_art': [],
                    'danceability': [],
                    'energy': [],
                    'key': [],
                    'loudness': [],
                    'mode': [],
                    'speechiness': [],
                    'acousticness': [],
                    'instrumentalness': [],
                    'liveness': [],
                    'valence': [],
                    'tempo': [],
                    'duration_ms': []}
# create an open dictionary to be able to receive all attributes


for item in results['items']:
#results is a massive dictionary results for each track in a playlist.  This loops through each result returned.
    track_id = item['track']['id']
    track_attributes['track_name'].append(item['track']['name'])
    #we don't need to slice the results list to [0] b/c we're already inside the list with the loop
    track_attributes['album_art'].append(item['track']['album']['images'][1]['url'])
    #album kjey has a nested list, so we need to slice @ [1] to get the 300x300px
    ind_track_attributes = sp.audio_features(track_id)[0]
    #the [0] accesses the nested dictionary inside the list

    track_attributes['track_id'].append(ind_track_attributes['id'])
    track_attributes['danceability'].append(ind_track_attributes['danceability'])
    track_attributes['energy'].append(ind_track_attributes['energy'])
    track_attributes['key'].append(ind_track_attributes['key'])
    track_attributes['loudness'].append(ind_track_attributes['loudness'])
    track_attributes['mode'].append(ind_track_attributes['mode'])
    track_attributes['speechiness'].append(ind_track_attributes['speechiness'])
    track_attributes['acousticness'].append(ind_track_attributes['acousticness'])
    track_attributes['instrumentalness'].append(ind_track_attributes['instrumentalness'])
    track_attributes['liveness'].append(ind_track_attributes['liveness'])
    track_attributes['valence'].append(ind_track_attributes['valence'])
    track_attributes['tempo'].append(ind_track_attributes['tempo'])
    track_attributes['duration_ms'].append(ind_track_attributes['duration_ms'])

# for key in track_attributes:
#     print(len(track_attributes[key]))
#     print(key)
# #test to see if we return all the same number of results


df = pd.DataFrame.from_dict(track_attributes)
print(df)
df.to_csv(r'track_attributes.csv', index = False)
exit()

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html

