# Azure FUnciton
import logging
import azure.functions as func

# App
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


# Azure Function

app = func.FunctionApp()

@app.timer_trigger(schedule="0 0 0 * * 6", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def TimerTriggerTop50Songs(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


playlist_id = "37i9dQZEVXbNBz9cRCSFkY"
endpoint=f"https://api.spotify.com/v1/playlists/{playlist_id}"

# Connect to Spotify API
token = get_token()
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

# Get rank, song name, song artist, album, released_date, etc 
track_rank = 1
for track in playlist_tracks:
    artists = ", ".join([ x["name"] for x in track["track"]["artists"] ])

    track_data = {
            'rank': track_rank,
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
    track_rank += 1

# Convert to list to a dataframe
songs_df = pd.DataFrame(tracks_data)
print(songs_df.head(5))