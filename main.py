import os
from random import seed
from webbrowser import get
from dotenv import load_dotenv
import spotipy
import json
import time

load_dotenv()

scope = "user-library-read"
oauth_object = spotipy.oauth2.SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"), 
                                           client_secret=os.getenv("SPOTIFY_PRIVATE"), 
                                           redirect_uri=os.getenv("URI"), 
                                           scope=scope
                                           )

token = oauth_object.get_cached_token()["access_token"]
Spotify_object = spotipy.Spotify(auth=token)


def get_Song_Infos():
    song_info = Spotify_object.current_user_playing_track()
    song_name = song_info["item"]["name"]
    album_name = song_info["item"]["album"]["name"]
    artist_name = song_info["item"]["artists"][0]["name"]
    song_link = song_info["item"]["external_urls"]["spotify"]
    CustomJson = {"Song" :song_name,"Album":album_name, "Artist":artist_name, "Link":song_link}
    return CustomJson

def recommendations(artists, genres, tracks):
    recommendations = Spotify_object.recommendations(seed_artists=artists,seed_genres=genres,seed_tracks=tracks, limit=20)
    return recommendations

# Writing to sample.json
with open("output.json", "w") as outfile:
    outfile.write(json.dumps(get_Song_Infos(), indent=4))