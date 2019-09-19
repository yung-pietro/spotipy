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

track_attributes = {'track_name': [], 'track_id': [], 'track_url': []}



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

#print(track_attributes)

df = pd.DataFrame.from_dict(track_attributes)
# df.to_csv(r'tracks.csv', index = False)
print(df.columns)

ids = df['track_id'].tolist()
for id in ids:
    print(id)
    print(sp.audio_features(id)[0]['loudness'])

# print(track_ids)
# checks the loop

# feature_test = sp.audio_features(track_ids[0])[0]
# print(feature_test)



exit()


# I'm able to slice (using [0] syntax) b/c the dictionary has an embedded list


# # ----------------------- Experimental -------------------------

# #Extract Artist's uri

# #Store artist's track' names' and uris in separate lists
# track_artist = []
# track_art = []
# track_names = []
# track_uris = []

# for i in range(len(results['items'])):
#     track_artist.append(results['items'][i]['track']['album']['artists']['name'])
#     track_art.append(results['items'][i]['track']['album']['images'][2]['url'])
#     track_names.append(results['items'][i]['track']['name'])
#     track_uris.append(results['items'][i]['track']['id'])


# album_names
# album_uris
# #Keep names and uris in same order to keep track of duplicate albums


# def trackUris(uri):
#     track = uri

# def audio_features(track):
#     #Add new key-values to store audio features
#     playlist_tracks['acousticness'] = []
#     playlist_tracks['danceability'] = []
#     playlist_tracks['energy'] = []
#     playlist_tracks['instrumentalness'] = []
#     playlist_tracks['liveness'] = []
#     playlist_tracks['loudness'] = []
#     playlist_tracks['speechiness'] = []
#     playlist_tracks['tempo'] = []
#     playlist_tracks['valence'] = []
#     playlist_tracks['popularity'] = []
#     #create a track counter
#     track_count = 0
#     for track in results['items']['track']['id']:
#         #pull audio features per track
#         features = sp.audio_features(track)
#         #Append to relevant key-value
#         playlist_tracks['acousticness'].append(features[0]['acousticness'])
#         playlist_tracks['danceability'].append(features[0]['danceability'])
#         playlist_tracks['energy'].append(features[0]['energy'])
#         playlist_tracks['instrumentalness'].append(features[0]['instrumentalness'])
#         playlist_tracks['liveness'].append(features[0]['liveness'])
#         playlist_tracks['loudness'].append(features[0]['loudness'])
#         playlist_tracks['speechiness'].append(features[0]['speechiness'])
#         playlist_tracks['tempo'].append(features[0]['tempo'])
#         playlist_tracks['valence'].append(features[0]['valence'])
#         #popularity is stored elsewhere
#         pop = sp.track(track)
#         playlist_tracks['popularity'].append(pop['popularity'])
#         track_count+=1

# # we need to:
# # 1. loop through our track results and using the URI, append
