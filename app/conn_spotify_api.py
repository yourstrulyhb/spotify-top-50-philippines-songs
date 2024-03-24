
import spotipy  
from spotipy.oauth2 import SpotifyOAuth  

# https://spotipy.readthedocs.io/en/2.22.1/#api-reference

SCOPE=""

sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)  

access_token = sp_oauth.get_access_token()  
refresh_token = sp_oauth.get_refresh_token()  
