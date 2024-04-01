"""
   Retrieve data from Spotify API
   and load to local Postgres database

   Data: Top 50 Songs - Philippines
   TODO: Set schedule, run Daily

   References:
   - https://www.datacamp.com/tutorial/tutorial-postgresql-python
   - https://www.geeksforgeeks.org/how-to-insert-a-pandas-dataframe-to-an-existing-postgresql-table/
"""
import os
import sys
from dotenv import load_dotenv
import base64 
from requests import post, get
import json
import pandas as pd 
from datetime import date
import numpy as np 
import psycopg2 
import psycopg2.extras as extras 


# Load environment variables 
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

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

   return songs_df


def load_to_postgres(tracks_df):
   db_pass = os.getenv('POSTGRES_DB_PASS')
   
   # Establish connection to database
   conn = psycopg2.connect(database = "spotify_api_db", 
                        user = "postgres", 
                        host= 'localhost',
                        password = db_pass,
                        port = 5432)

   table_name = "stg_top_50_songs_ph"
   cols = 'song_rank, title, spotify_id, artists, date_gathered,  popularity, album_name, album_release_date, album_spotify_id'

   row_tuples = [tuple(x) for x in tracks_df.to_numpy()] 
  
   # SQL query to execute 
   query = "INSERT INTO %s(%s) VALUES %%s" % (table_name, cols) 
   cursor = conn.cursor() 
   
   try: 
        extras.execute_values(cursor, query, row_tuples) 
        conn.commit() 
   
   except (Exception, psycopg2.DatabaseError) as error: 
        print("Error: %s" % error) 
        conn.rollback() 
        cursor.close() 
        return 1

   print("The dataframe is inserted") 
   cursor.close() 
  


if __name__ == "__main__":

   # Connect to Spotify API
   token = get_token()
   playlist_id = "37i9dQZEVXbNBz9cRCSFkY"   

   # Get tracks
   tracks = get_playlist_tracks(token=token, playlist_id=playlist_id)

   # Save to Postgres database
   load_to_postgres(tracks)

