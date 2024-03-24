"""
   Retrieve data from Spotify API
   Weekly Top 50
"""
from dotenv import load_dotenv
import os
import base64 
from requests import post, get
import json
import pandas as pd 
from datetime import date
 

# Load environment variables 
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(f'client_id={client_id}, client_secret={client_secret}')


def get_token():
   auth_string = client_id + ":" + client_secret
   auth_bytes = auth_string.encode("utf-8")
   auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

   url = "https://accounts.spotify.com/api/token"
   # "https://api.spotify.com/v1/playlists/{playlist_id}"


   headers = {
      "Authorization": "Basic " + auth_base64,
      "Content-Type": "application/x-www-form-urlencoded"
   }
   data = {"grant_type": "client_credentials"}
   result = post(url, headers=headers, data=data)
   json_result = json.loads(result.content)
   token = json_result["access_token"]

   return token



def get_auth_header(token):
   return {"Authorization": "Bearer " + token}


def get_top_50_philippines(token):
   playlist_id = "37i9dQZEVXbNBz9cRCSFkY"
   endpoint=f"https://api.spotify.com/v1/playlists/{playlist_id}"

   headers =  get_auth_header(token)
   
   result = get(endpoint, headers=headers)
   json_result = json.loads(result.content)["tracks"]["items"]


   songs = []

   today = date.today()


   # Get song name, song artist, released_date, album
   for track in json_result:
      
      artists = ", ".join([ x["name"] for x in track["track"]["artists"] ])

      track_data = {
            'song_title': track["track"]["name"],
            'song_spotify_id': track["track"]["id"],
            'artists': artists,
            'date_gathered': today,
            'popularity': track["track"]["popularity"],
            'album_name': track["track"]["album"]["name"],
            'album_release_date': track["track"]["album"]["release_date"],
            'album_spotify_id': track["track"]["album"]["id"]
      }

      songs.append(track_data)


   df = pd.DataFrame(songs)
   df.to_csv("songs_data.csv")

   print(df)
   print(len(json_result))



token = get_token()
# print(f"token={token}")


print(get_top_50_philippines(token))

