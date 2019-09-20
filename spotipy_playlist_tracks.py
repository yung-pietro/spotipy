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
import pandas as pd 


client_id = "866e67d3c5924baca1114ed5bc4eef50"
client_secret = "c6e2baa4ecac47cc9ecd6bf7dced31f4"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = "1252709106"
playlist_id = '37i9dQZF1E8Gd0iQSccTIC'
offset = 0


results = sp.user_playlist_tracks(username, playlist_id, fields=None, limit=100, offset=offset, market=None)
# Currently outputs a dictionary with (embedded lists and dicts) containing track info.  Things like identifying URI, album art, etc. I want to loop through each track listing and, using
#the identifying URI, grab track info.

#print(json.dumps(results, indent=4))
#shows the full dump

# print(results['items'][0]['track']['id'])
#demo accessing a single dictionary item

# print the type of the object 
# print(type(results['items']))
track_ids = []

# create a dictionary with ID and attributes of a single track

track_attributes = {'track_name': [], 
                    'track_id': [], 
                    'track_url': [], 
                    'danceability': [], 
                    'energy': [], 
                    'key': [], 
                    'loudness': [], 
                    'mode': [], 
                    'speechiness': [],
                    'acousticness': [],
                    'instrumental': [],
                    'liveness': [],
                    'valence': [],
                    'tempo': [],
                    'duration_ms': [] }

id_list_hack = []

for item in results['items']:
    # print(type(item))
    #determine what type of element each item is

    #print(item['track']['id'])
    #prints a list of track ids

    #track_ids.append(item['track']['id'])
    # appending track ids to the list we created earlier

    track_attributes['track_name'].append(item['track']['name'])
    track_attributes['track_id'].append(item['track']['id'])
    track_attributes['track_url'].append(item['track']['external_urls']['spotify'])
    id_list_hack.append(item['track']['id'])

# perhaps, first build the dictionary, then add things like above

list = 0
for id in id_list_hack:
    att_add = sp.audio_features(id)
    track_attributes[list]['energy'].append(att_add['energy'])
    track_attributes[list]['key'].append(att_add['key'])
    track_attributes[list]['loudness'].append(att_add['loudness'])
    track_attributes[list]['mode'].append(att_add['mode'])
    track_attributes[list]['speechiness'].append(att_add['speechiness'])
    track_attributes[list]['acousticness'].append(att_add['acousticness'])
    track_attributes[list]['instrumental'].append(att_add['instrumental'])
    track_attributes[list]['liveness'].append(att_add['liveness'])
    track_attributes[list]['valence'].append(att_add['valence'])
    track_attributes[list]['tempo'].append(att_add['tempo'])
    track_attributes[list]['duration_ms'].append(att_add['duration'])
    list += 1

df = pd.DataFrame.from_dict(track_attributes)
print(df)
df.to_csv(r'track_attributes.csv', index = False)
   
    #print(id)
    #print(sp.audio_features(id)[0]['loudness'])


# df2.to_csv(r'attributes-example.csv', index=False)

# print(track_ids)
# checks the loop

# feature_test = sp.audio_features(track_ids[0])[0]
# print(feature_test)



#exit()
#Use this for segmented testing


# I'm able to slice (using [0] syntax) b/c the dictionary has an embedded list


