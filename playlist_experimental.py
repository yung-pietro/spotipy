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
