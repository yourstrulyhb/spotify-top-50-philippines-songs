"""
   Retrieve data from Spotify API
   Top 50 Songs - Philippines
   Run Weekly
"""

from dotenv import load_dotenv
import os
import base64 
from requests import post, get
import json
import pandas as pd 
import sys
from datetime import date
 
# Load environment variables 
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

TODAY = date.today()
playlist_title = "0"


def get_token() -> str:
   auth_string = client_id + ":" + client_secret
   auth_bytes = auth_string.encode("utf-8")
   auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

   url = "https://accounts.spotify.com/api/token"

   headers = {
      "Authorization": "Basic " + auth_base64,
      "Content-Type": "application/x-www-form-urlencoded"
   }
   data = {"grant_type": "client_credentials"}
   result = post(url, headers=headers, data=data)
   json_result = json.loads(result.content)
   token = json_result["access_token"]

   return token


def get_auth_header(token: str) -> str:
   return {"Authorization": "Bearer " + token}


def get_playlist_tracks(token: str, playlist_id: str) -> pd.DataFrame:
   """
   Return a DataFrame of songs data
   """

   endpoint=f"https://api.spotify.com/v1/playlists/{playlist_id}"
   headers =  get_auth_header(token)
   

   playlist_tracks = []
   try: 
      result = get(endpoint, headers=headers)
      playlist_title = json.loads(result.content)["name"]
      print(playlist_title)
      
      playlist_tracks = json.loads(result.content)["tracks"]["items"]

   except:
      return pd.DataFrame()   # Return empty dataframe


   tracks_data = []           # List that will contain relevant track data

   # Get song name, song artist, album, released_date, etc 
   for track in playlist_tracks:
      artists = ", ".join([ x["name"] for x in track["track"]["artists"] ])

      track_data = {
            'song_title': track["track"]["name"],
            'song_spotify_id': track["track"]["id"],
            'artists': artists,
            'date_gathered': TODAY,
            'popularity': track["track"]["popularity"],
            'album_name': track["track"]["album"]["name"],
            'album_release_date': track["track"]["album"]["release_date"],
            'album_spotify_id': track["track"]["album"]["id"]
      }

      tracks_data.append(track_data)


   # Convert to list to a dataframe
   songs_df = pd.DataFrame(tracks_data)

   return songs_df


if __name__ == "__main__":

   # Connect to Spotify API
   token = get_token()
   
   # Set playlist_id
   playlist_id = ""
   try: 
      param = sys.argv[1]
      playlist_id = param        # Set playlist_id to one passed in parameter 

   except:
       playlist_id = "37i9dQZEVXbNBz9cRCSFkY"      # Defualt playlist id: 


   # Get tracks
   tracks = get_playlist_tracks(token=token, playlist_id=playlist_id)

   if not tracks.empty:
      print(tracks[['song_title', 'artists', 'album_name', 'album_release_date']]) 

       # Save to CSV file
      csv_filename = str(TODAY) + "_playlist_data_" + playlist_id + ".csv"    # e.g. 03-26-2024_playlist_data_37i9dQZEVXbNBz9cRCSFkY.csv
      tracks.to_csv(csv_filename)
   
   else:
      print("Could not find playlist.")
  
