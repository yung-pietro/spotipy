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


# create a dictionary with ID and attributes of a single track

track_attributes = { 
                    'track_name': [], 
                    'track_id': [],
                   # 'track_url': [], 
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


for item in results['items']:
    # id_list.append(item['track']['id'])
    track_id = item['track']['id']
    track_attributes['track_name'].append(item['track']['name'])
    #track_attributes['track_url'].append(item['track']['url'])
    track_attributes['album_art'].append(item['track']['album']['images'][1]['url'])
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

for key in track_attributes:
    print(len(track_attributes[key]))
    print(key)
# print(track_attributes)

# for key, value in track_attributes.items():
#     print(len(value))
# exit()

# test = sp.audio_features(id_list[0])
# print(f"Features of {id_list[0]} are: ")
# print(test)


    # track_attributes['track_name'].append(item['track']['name'])
    # track_attributes['track_id'].append(item['track']['id'])
    # track_attributes['track_url'].append(item['track']['external_urls']['spotify'])
    #id_list_hack.append(item['track']['id'])


df = pd.DataFrame.from_dict(track_attributes)
print(df)
df.to_csv(r'track_attributes.csv', index = False)
exit() 
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


