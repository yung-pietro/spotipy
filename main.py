import spotipy
#imports Spotipy: https://spotipy.readthedocs.io
from spotipy.oauth2 import SpotifyClientCredentials
#pulls in Spotipy's Oauth2 module SpotifyClientCredentials

client_id = '866e67d3c5924baca1114ed5bc4eef50'
client_secret = 'c6e2baa4ecac47cc9ecd6bf7dced31f4'
#How do I obscure these so that they can't be seen by public eyes

credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
#credentials_manager is a new *object* from the SpotifyClientCredentials *class*.
# To understand more about the class, we can search in the Spotipy docs: https://spotipy.readthedocs.io/en/latest/?highlight=spotifyclientcredentials#spotipy.oauth2.SpotifyClientCredentials
# Or search in the codebase.  All module files reside in the site-packages folder

sp = spotipy.Spotify(client_credentials_manager=credentials_manager)
#Spotify object to access API
#same as above.  Question is, why do we need to import SpotifyClientCredentials, but not spotipy.Spotify



name = "Lane 8"

result = sp.search(name) #search query
#search is a function found in spotipy
print(result['tracks']['items'][0]['artists'])

#This code relates to this library: https://spotipy.readthedocs.io/en/latest/#
#I'm  trying to follow this tutorial: https://medium.com/@RareLoot/extracting-spotify-data-on-your-favourite-artist-via-python-d58bc92a4330
#I'm will be querying this API: https://developer.spotify.com/documentation/web-api/
